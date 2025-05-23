import urllib.parse
# Attempt to import googlesearch, provide instructions if it fails.
try:
    from googlesearch import search
except ImportError:
    print("Module 'googlesearch' not found. Please install it using 'pip install googlesearch-python'")
    # If the import fails, functions relying on 'search' will not be usable.
    search = None # Placeholder if import fails

def get_search_urls(career_title: str) -> dict:
    """
    Constructs and returns a dictionary of Google search URLs for a given career title.
    """
    encoded_title = urllib.parse.quote_plus(career_title)
    
    urls = {
        "General Information": f"https://www.google.com/search?q={encoded_title}+description+overview",
        "Typical Skills": f"https://www.google.com/search?q=typical+skills+for+{encoded_title}",
        "Current Job Postings": f"https://www.google.com/search?q={encoded_title}+jobs",
        "Salary Information": f"https://www.google.com/search?q={encoded_title}+salary",
        "Career Path": f"https://www.google.com/search?q={encoded_title}+career+path"
    }
    return urls

def fetch_career_info(career_title: str) -> dict:
    """
    Fetches top search result URLs for a given career title using the googlesearch library.
    Returns a dictionary with lists of formatted strings containing these URLs.
    """
    if not search:
        # This message format aligns with how other parts of the system might expect errors.
        unavailable_message = ["'googlesearch' library not available or import failed."]
        return {
            "description": unavailable_message,
            "skills_info": unavailable_message,
            "job_postings_info": unavailable_message,
            "salary_info": unavailable_message, # Added as per get_search_urls
            "career_path_info": unavailable_message # Added as per get_search_urls
        }

    results = {
        "description": [],
        "skills_info": [],
        "job_postings_info": [],
        "salary_info": [],
        "career_path_info": []
    }

    # Define queries
    queries = {
        "description": f"{career_title} description overview",
        "skills_info": f"typical skills for {career_title}",
        "job_postings_info": f"{career_title} jobs",
        "salary_info": f"{career_title} salary",
        "career_path_info": f"{career_title} career path"
    }

    for key, query in queries.items():
        try:
            # Using tld="com", lang="en" for consistency
            # num_results=2 to get top 2 results as suggested.
            # stop=2 is equivalent to num_results=2 for this library's basic usage.
            # pause=2.0 is a polite delay between requests.
            search_results = list(search(query, num_results=2, lang="en", pause=2.0)) 
            if search_results:
                for url in search_results:
                    # The library directly returns URLs.
                    # The prompt was updated to reflect that titles/snippets are not directly available.
                    results[key].append(f"Search result URL: {url}")
            else:
                results[key].append(f"No search results found for: {query}")
        except Exception as e:
            # Provide a more specific error message for the category
            results[key].append(f"Error fetching {key.replace('_', ' ')}: {str(e)}")
            
    return results

if __name__ == '__main__':
    # Example Usage (for testing purposes)
    if search: # Only run if the library is available
        print("--- Example: get_search_urls ---")
        example_urls = get_search_urls("Software Developer")
        for k, v in example_urls.items():
            print(f"{k}: {v}")
        
        print("\n--- Example: fetch_career_info ---")
        # Be mindful of making too many requests if running this frequently.
        # This example is for demonstration; actual use might be rate-limited by Google.
        try:
            career_info = fetch_career_info("Data Scientist")
            for category, info_list in career_info.items():
                print(f"\n{category.replace('_', ' ').title()}:")
                if info_list:
                    for item in info_list:
                        print(item)
                else:
                    print("No information retrieved.")
        except Exception as e:
            print(f"An error occurred during fetch_career_info example: {e}")
    else:
        print("googlesearch library not available, skipping examples.")
