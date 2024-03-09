from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from typing import Dict
from pydantic import BaseModel, Field
from utils import save_to_md_file


class ResponseOutput(BaseModel):
    text: str = Field(description="markdown resume")
    job_description_name: str = Field(description="job description name in about 5 words")

response_output_parser = PydanticOutputParser(pydantic_object=ResponseOutput)


def get_generate_resume_prompt_template():
    prompt = PromptTemplate(
        template="""Given the job description: 
{job_description}

Update the following resume (given in markdown) to align more closely with the job description. Do not change the format of the resume.
Resume:
{resume_content}

{format_instructions}

Updated Resume:
""",
        input_variables=["job_description", "resume_content"],
        partial_variables={
            "format_instructions": response_output_parser.get_format_instructions()
        },
    )
    return prompt


def generate_resume_with_job_description(job_description, resume_content=None, llm=None):
    if not resume_content:
        ## get resume content from file resume_md/main.md
        with open("resume_md/0_Main.md", "r") as file:
            resume_content = file.read()
    
    x = {
        "resume_content": resume_content,
        "job_description": job_description,
    }

    generate_resume_prompt_template = get_generate_resume_prompt_template()
    generate_resume_chain = (
        generate_resume_prompt_template | llm | response_output_parser
    )
    response = generate_resume_chain.invoke(x)
    response = ResponseOutput.parse_obj(response)

    text = response.text
    job_description_name = response.job_description_name

    filename = save_to_md_file(job_description_name=job_description_name, text=text)
    return filename


if __name__ == "__main__":
    from utils import get_llm
    from dotenv import load_dotenv
    load_dotenv('./.env')

    llm = get_llm(max_tokens=2000)

    job_description = '''
Data Scientist-Senior Associate - P&T Labs
PwC Service Delivery Center

Job description

    A career in Products and Technology is an opportunity to bring PwCs strategy to life by driving products and technology into everything we deliver
    Our clients expect us to bring the right people and the right technology to solve their biggest problems; Products and Technology is here to help PwC meet that challenge and accelerate the growth of our business
    We have skilled technologists, data scientists, product managers and business strategists who are using technology to accelerate change
    Our team collaborates with product strategy and product managers to govern readiness standards in achieving principles (compliance, privacy, security) by design for what PwCs technology assets require to be successful in the market
    They provide guidance for product development across the lifecycle (ideation / strategy through commercialization / monetization)
    Additionally, they facilitate market readiness for technology assets overall, as changes occur to assets or market conditions throughout the asset's life cycle

Day to day responsibility:

    Design and develop solutions related to machine learning, natural language processing and deep learning & Generative AI to address business needs.
    Daily the team utilizes the latest technologies to work creatively and analytically to apply cutting edge techniques to specific challenges
    You need exceptional skills in data science and continuously expand personal skill sets and stay up to speed on the latest A.I. trends, tools, methodologies, and techniques.

Skills and Experience

    Demonstrates thorough abilities and/or a proven record of success as a team leader including:

Must Have

    Ideally 4 to 6 years of relevant experience.
    bachelors Degree in Computer Science, Engineering or other technical discipline (BE, BTech, MCA).
    Performing in development language environments- eg Python, Java, Scala, R, SQL, etc and applying analytical methods to large and complex datasets leveraging one of those languages
    Candidate should have a solid work exposure to Generative AI based projects that includes designing and implementing solutions based on Langchain framework and designing efficient prompt for LLMs.
    Candidate should have good experience in pre-training and fine tuning Large Language Models (LLMs) on HuggingFace models & other Large Language Models.
    Candidate should have prior experience on Azure cloud platform.
    Experience in machine learning, natural language processing and deep learning.
    Proven ability with NLP and text-based extraction techniques.
    Familiarity with deep learning architectures used for text analysis, computer vision and signal processing.
    Understanding of not only how to develop data science analytic models but how to operationalize these models so they can run in an automated context
    Understanding of machine learning algorithms, such as k-NN, GBM, Neural Networks Naive Bayes, SVM, and Decision Forests.
    Utilizing and applying knowledge commonly used data science packages including Spark, Pandas, SciPy, and NumPy.
    Leading, training and working with other data scientists in designing effective analytical approaches taking into consideration performance and scalability to large datasets
    Experience manipulating and analyzing complex, high-volume, high-dimensionality data from varying sources
    Applying techniques such as multivariate regressions, Bayesian probabilities, clustering algorithms, machine learning, dynamic programming, stochastic-processes, queuing theory, algorithmic knowledge to efficiently research and solve complex development problems and application of engineering methods to define, predict and evaluate the results obtained.
    Developing and deploying A.I. solutions as part of a larger automation pipeline

Good to Have

    Demonstrates extensive abilities and/or a proven record of success in the application of statistical modelling, algorithms, data mining and machine learning algorithms problem solving
    A track record of delivery within a number of large-scale projects, demonstrating ownership of architecture solutions and managing change
    Utilizing programming skills and knowledge on how to write models which can be directly used in production as part of a large-scale system.
    Utilizing and applying knowledge of technologies such as H20.ai, Google Machine Learning and Deep learning.
    Developing end to end deep learning solutions for structured and unstructured data problems.
    Using common cloud computing platforms including Azure, AWS and GCP in addition to their respective utilities for managing and manipulating large data sources, model, development, and deployment.
    Visualizing and communicating analytical results, using technologies such as HTML, JavaScript, D3, Tableau, and PowerBI.

Other Skills

    Documenting systems, refining requirements, self-identify solutions and communicate to the team;
    Demonstrating a desire to keep learning, maintain own skill set, stay up to date and expand one's knowledge across the full stack;
    Demonstrating a desire to improve the status quo , especially automating and improving software development and operations processes to achieve massively higher delivery velocity and operations quality;
    Contributing to thought leadership through participation in the development of technology processes;
    Applying continuous independent judgement while collaborating with others, and influencing others within the project and domain teams; and,
    Building and leveraging relationships as well as specialist level verbal and written communication skills.

Preferred Certifications (at least two certifications are preferred):

    Data Science Certifications in Machine Learning, Deep Learning and Natural Language Processing.
    Certified Professional in Python Programming Level 1 or 2

Role: Data Scientist
Industry Type: Accounting / Auditing
Department: Data Science & Analytics
Employment Type: Full Time, Permanent
Role Category: Data Science & Machine Learning
Education
UG: B.Tech/B.E. in Any Specialization, Any Graduate
PG: LLM in Law, MCA in Computers
Key Skills
'''

    generate_resume_with_job_description(job_description=job_description, llm=llm)
