# ChatGPT plugins quickstart

This is a ChatGPT plugin using Python that gets the content of a website. Might not work for all sites but I am open to PRs. This plugin is designed to work in conjunction with the [ChatGPT plugins documentation](https://platform.openai.com/docs/plugins). If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup locally

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

Download chromedrive.exe according to your Chrome Browser version from [Chrome WebDriver Downloads](https://chromedriver.chromium.org/downloads) and place it into the root of the folder

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "Give me the summary of https://spokesman-recorder.com/2023/06/02/the-future-of-work-education-and-ai/" and then you can ask questions about the content! 

## Setup remotely

### Cloudflare workers

### Code Sandbox

### Replit

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
