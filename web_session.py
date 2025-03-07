import webbrowser
import sys

def open_urls_in_browser(file_path, browser_name=None):
    try:
        if browser_name:
            browser = webbrowser.get(browser_name)
        else:
            browser = webbrowser.get()
        
        with open(file_path, 'r') as file:
            urls = file.readlines()
            for line in urls:
                url = line.strip().split()[0]  # Split by space and take the first part
                if url.startswith("http"):
                    browser.open_new_tab(url)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python web_session.py <file_path> [chrome|firefox|safari|edge|windows-default|opera]")
    else:
        file_path = sys.argv[1]
        browser_name = sys.argv[2] if len(sys.argv) == 3 else None
        open_urls_in_browser(file_path, browser_name)