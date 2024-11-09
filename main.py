# from bs4 import BeautifulSoup
# import requests
# import time

# url = 'https://www.cricbuzz.com/live-cricket-scores/108771/ban-vs-afg-2nd-odi-afghanistan-v-bangladesh-in-uae-2024'

# while True:
#     time.sleep(10)
    
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     score_card = soup.find('div', class_='cb-min-bat-rw').span.text

#     print("Current Score Is \n {}".format(score_card))


# from bs4 import BeautifulSoup
# import requests
# import time

# url = 'https://www.cricbuzz.com/live-cricket-scores/108771/ban-vs-afg-2nd-odi-afghanistan-v-bangladesh-in-uae-2024'

# while True:
#     try:
#         time.sleep(10)  # Waits for 10 seconds before each request
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'lxml')

#         # Locate the score information in the HTML
#         score_card = soup.find('div', class_='cb-min-bat-rw').span.text

#         # HTML content for displaying the score
#         html_content = f"""
#         <html>
#         <head>
#             <title>Live Cricket Score</title>
#             <style>
#                 body {{ font-family: Arial, sans-serif; }}
#                 .score-container {{ margin: 50px auto; text-align: center; }}
#                 h1 {{ color: #333; }}
#             </style>
#         </head>
#         <body>
#             <div class="score-container">
#                 <h1>Current Score</h1>
#                 <p>{score_card}</p>
#             </div>
#         </body>
#         </html>
#         """

#         # Overwrite the existing HTML file with the latest score
#         with open('live_score.html', 'w') as file:
#             file.write(html_content)

#         print("Current Score: ", score_card)

#     except Exception as e:
#         print("An error occurred:", e)


from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.cricbuzz.com/live-cricket-scores/108771/ban-vs-afg-2nd-odi-afghanistan-v-bangladesh-in-uae-2024'

while True:
    try:
        time.sleep(4)  # Waits for 10 seconds before each request
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Locate the score information in the HTML
        score_card = soup.find('div', class_='cb-min-bat-rw').span.text

        # HTML content for displaying the score, with meta refresh for auto-refresh in the browser
        html_content = f"""
        <html>
        <head>
            <title>Live Cricket Score</title>
            <meta http-equiv="refresh" content="4"> <!-- Refreshes page every 4 seconds -->
            <style>
                body {{ font-family: Arial, sans-serif; }}
                .score-container {{ margin: 50px auto; text-align: center; }}
                h1 {{ color: #333; }}
            </style>
        </head>
        <body>
            <div class="score-container">
                <h1>Current Score</h1>
                <p>{score_card}</p>
            </div>
        </body>
        </html>
        """

        # Overwrite the existing HTML file with the latest score
        with open('live_score.html', 'w') as file:
            file.write(html_content)

        print("Current Score: ", score_card)

    except Exception as e:
        print("An error occurred:", e)
