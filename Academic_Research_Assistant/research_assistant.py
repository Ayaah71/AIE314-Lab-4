# research_assistant.py
import wikipedia
import arxiv

# Wikipedia search
def wikipedia_search(topic):
    try:
        return wikipedia.summary(topic, sentences=5)
    except:
        return "No Wikipedia information found"

# arXiv search
def arxiv_search(topic):
    search = arxiv.Search(query=topic, max_results=2)
    papers = [paper.summary for paper in search.results()]
    return "\n".join(papers)

# Generate structured report
def generate_report(topic):
    wiki = wikipedia_search(topic)
    papers = arxiv_search(topic)
    
    report = f"""
RESEARCH REPORT

Topic: {topic}

Introduction:
{wiki}

Research Findings:
{papers}

Conclusion:
Summary of key insights on {topic}

Sources:
Wikipedia
arXiv
"""
    return report

# Chat system
def research_assistant():
    print("Academic Research Assistant")
    print("Type 'exit' to stop\n")
    
    while True:
        topic = input("Research Topic: ")
        if topic.lower() == "exit":
            break
        report = generate_report(topic)
        print(report)

# Run assistant
if __name__ == "__main__":
    research_assistant()