import json
import random
from faker import Faker

fake = Faker()

# Create sales_leads.json
leads = [{'lead_id': i, 'name': fake.name(), 'email': fake.email(), 'company': fake.company(), 'contacted': False} for i in range(1, 101)]
with open('sales_leads.json', 'w') as f:
    json.dump(leads, f)

# Create sales_opportunities.json
opportunities = [{'opp_id': i, 'name': fake.name(), 'value': round(random.uniform(5000.0, 20000.0), 2), 'stage': random.choice(['Discovery', 'Proposal', 'Negotiation'])} for i in range(1, 101)]
with open('sales_opportunities.json', 'w') as f:
    json.dump(opportunities, f)

# Create nps_submissions.json
nps_submissions = [{'submission_id': i, 'customer_id': i, 'score': random.randint(0, 10), 'feedback': fake.text(max_nb_chars=200)} for i in range(1, 101)]
with open('nps_submissions.json', 'w') as f:
    json.dump(nps_submissions, f)

# Create support_tickets.json
tickets = [{'ticket_id': i, 'customer_id': i, 'issue': fake.text(max_nb_chars=100), 'status': random.choice(['Open', 'Closed', 'Pending'])} for i in range(1, 101)]
with open('support_tickets.json', 'w') as f:
    json.dump(tickets, f)

# Create marketing_blogs.json
blogs = [{'blog_id': i, 'title': fake.text(max_nb_chars=50), 'author': fake.name(), 'content': fake.text(max_nb_chars=1000)} for i in range(1, 101)]
with open('marketing_blogs.json', 'w') as f:
    json.dump(blogs, f)

# Create newsletter_subscribers.json
subscribers = [{'subscriber_id': i, 'name': fake.name(), 'email': fake.email()} for i in range(1, 101)]
with open('newsletter_subscribers.json', 'w') as f:
    json.dump(subscribers, f)