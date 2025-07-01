from gradio_client import Client

# Initialize the client for the Hugging Face Space
client = Client("sahilawatramani/crime-analytics-backend")

def gr_query(query):
    """
    Calls the /gr_query endpoint with the provided query string.
    Returns the chatbot response as a string.
    """
    return client.predict(query=query, api_name="/gr_query")

def gr_quick_stats():
    """
    Calls the /gr_quick_stats endpoint.
    Returns quick stats as a dict/list/str/float/bool.
    """
    return client.predict(api_name="/gr_quick_stats")

def gr_filter_options():
    """
    Calls the /gr_filter_options endpoint.
    Returns filter options as a dict/list/str/float/bool.
    """
    return client.predict(api_name="/gr_filter_options")

def gr_sample_queries():
    """
    Calls the /gr_sample_queries endpoint.
    Returns sample queries as a dict/list/str/float/bool.
    """
    return client.predict(api_name="/gr_sample_queries")

def gr_debug():
    """
    Calls the /gr_debug endpoint.
    Returns debug info as a dict/list/str/float/bool.
    """
    return client.predict(api_name="/gr_debug")

if __name__ == "__main__":
    # Example usage
    print("/gr_query:", gr_query("Hello!!"))
    print("/gr_quick_stats:", gr_quick_stats())
    print("/gr_filter_options:", gr_filter_options())
    print("/gr_sample_queries:", gr_sample_queries())
    print("/gr_debug:", gr_debug()) 