import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

def initial_data():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS jobs(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        job_title TEXT,
                        location TEXT,
                        job_description TEXT,
                        application_link TEXT,
                        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(job_title, company_name, location)
                        )
                        """)
    conn.commit()
    conn.close()
def fetch_jobs():
    url = "https://realpython.github.io/fake-jobs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    jobs = []
    for job in soup.find_all("div", class_="card-content"):
        title = job.find("h2", class_="title").get_text(strip=True)
        company = job.find("h3", class_="company").get_text(strip=True)
        location = job.find("p", class_="location").get_text(strip=True)
        description = job.find("div", class_="description").get_text(strip=True)
        application_link = job.find("a", text="Apply")["href"]
        
        jobs.append((title, company, location, description, application_link))
    
    return jobs
def update_data(jobs):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    for job in jobs:
        cursor.execute('''
            INSERT INTO jobs (job_title, company_name, location, job_description, application_link, last_updated)
            VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(job_title, company_name, location) 
            DO UPDATE SET job_description=excluded.job_description, application_link=excluded.application_link, last_updated=CURRENT_TIMESTAMP
        ''', job)
    
    conn.commit()
    conn.close()

def export_to_csv(filename, company=None, location=None):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    query = "SELECT job_title, company_name, location, job_description, application_link FROM jobs WHERE 1=1"
    params = []
    
    if company:
        query += " AND company_name = ?"
        params.append(company)
    if location:
        query += " AND location = ?"
        params.append(location)
    
    cursor.execute(query, params)
    jobs = cursor.fetchall()
    conn.close()
    
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Job Description", "Application Link"])
        writer.writerows(jobs)

if __name__ == "__main__":
    initial_data()
    job_list = fetch_jobs()
    update_data(job_list)
    export_to_csv("filtered_jobs.csv")