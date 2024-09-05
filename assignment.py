import urllib.request

def fetch_html(url):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
    return html
def extract_stories(html_content):
    # Manually parsing to extract story links or titles
    stories = []
    
    # Assuming we are looking for <a> tags in the stories section
    start_index = html_content.find('<section class="latest-stories">')  # Find where the latest stories section starts
    if start_index != -1:
        # Extract part of the HTML containing stories
        end_index = html_content.find('</section>', start_index)
        section_html = html_content[start_index:end_index]
        
        # Manually searching for story titles in <a> tags (this is a simplified example)
        for i in range(6):  # We only need the top 6 stories
            link_start = section_html.find('<a href=', start_index)
            link_end = section_html.find('</a>', link_start)
            
            if link_start == -1:
                break  # No more stories found
            
            # Extracting the link text (or title)
            story_link = section_html[link_start+9:link_end]  # Adjust according to actual HTML structure
            stories.append(story_link)
            start_index = link_end
        
    return stories
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/latest-stories', methods=['GET'])
def get_latest_stories():
    url = "https://time.com"  # Example URL
    html_content = fetch_html(url)
    latest_stories = extract_stories(html_content)
    
    return jsonify({
        "stories": latest_stories
    })

if __name__ == '__main__':
    app.run(debug=True)
ass,ll