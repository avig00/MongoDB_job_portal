# Import packages
import pandas as pd
import json

# Define the schema
schema = {
    "Company_and_industry_info": {
        "_id": "_id", 
        "industry_name": "industry_name",
        "growth_rate": "growth_rate",
        "industry_skill": "industry_skill",
        "top_companies": "top_companies",
        "trends": "trends",
        "name": "name",
        "size": "size",
        "type": "type",
        "location": "location",
        "website": "website",
        "description": "description",
        "hr_contact": "hr_contact",
    },

    "Listings": {
        "_id": "_id",
        "employment_type": "employment_type",
        "average_salary": "average_salary",
        "benefits": "benefits",
        "remote": "remote",
        "job_posting_url": "job_posting_url",
        "posting_date": "posting_date",
        "closing_date": "closing_date",
        "title": "title",
        "description": "description",
        "years_of_experience": "years_of_experience",
        "detailed_description": "detailed_description",
        "responsibilities": "responsibilities",
        "requirements": "requirements",
        "required_education": "required_education",
        "preferred_skills": "preferred_skills",
    }
}

# Load CSV data into pandas dataframes
jobs_df = pd.read_csv("./data/jobs.csv")
companies_df = pd.read_csv("./data/companies.csv")
education_df = pd.read_csv("./data/education_and_skills.csv")
employment_df = pd.read_csv("./data/employment_details.csv")
industry_df = pd.read_csv("./data/industry_info.csv")


# Convert df columns with strings separated by commas into a list
jobs_df['requirements'] = jobs_df['requirements'].str.split(', ').apply(lambda x: list(set([i.strip() for i in x if i.strip() != ''])))
education_df['preferred_skills'] = education_df['preferred_skills'].str.split(', ').apply(lambda x: list(set([i.strip() for i in x if i.strip() != ''])))
employment_df['benefits'] = employment_df['benefits'].str.split(', ').apply(lambda x: list(set([i.strip() for i in x if i.strip() != ''])))
industry_df['industry_skills'] = industry_df['industry_skills'].str.split(', ').apply(lambda x: list(set([i.strip() for i in x if i.strip() != ''])))
industry_df['top_companies'] = industry_df['top_companies'].str.split(', ').apply(lambda x: list(set([i.strip() for i in x if i.strip() != ''])))
industry_df['trends'] = industry_df['trends'].str.split(', ').apply(lambda x: list(set([i.strip() for i in x if i.strip() != ''])))

# Merge the dataframes to match the required schema
# Merge compnay and industry data
merged_companies_industry_df = pd.merge(industry_df, companies_df, on="id", how="inner")
# Merge education, jobs, and employment data
merged_listings_df = pd.merge(education_df, jobs_df, left_on='job_id', right_on='id', how='inner')
merged_listings_df = pd.merge(merged_listings_df, right=employment_df, left_on='id_x', right_on='id', how='inner')
# Drop unwanted extra id columns from merged listings data frame
merged_listings_df.drop(['id_x', 'id_y'], axis=1, inplace=True)

# Convert merged dataframes to dictionaries using the schema
company_and_industry_info = merged_companies_industry_df.rename(columns=schema["Company_and_industry_info"]).to_dict(orient="records")
listings = merged_listings_df.rename(columns=schema["Listings"]).to_dict(orient="records")

# Create JSON files for the merged data
with open("./data/company_and_industry_info.json", "w") as company_industry_file:
    json.dump(company_and_industry_info, company_industry_file, indent=4)

with open("./data/listings.json", "w") as listings_file:
    json.dump(listings, listings_file, indent=4)


