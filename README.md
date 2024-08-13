# Paris Olympics 2024 Dashboard
The 2024 Summer Olympics, officially the Games of the XXXIII Olympiad and branded as Paris 2024, is an international multi-sport event that are occuring from 24 July to 11 August 2024 in France, with the opening ceremony having taken place on 26 July.
To provide comprehensive overview of Paris 2024 to audiences, particularly on tracking medals by countries, sports and athletes
To convince stakeholders of the dashboard’s potential for profitability

# How to Run
## Deployed Version
This web dashboard is deployed on the following URL: [Paris Olympics 2024 Web Dashboard](http://206.189.89.80/)

Sample login credentials:
- Username: admin
- Password: admin

## To Run Locally
1. Install docker and docker compose
2. Run in command line:
   <pre>
   docker compose up --build --detach
   </pre>
3. Open in your web browser: http://localhost:80

### Known issues when running locally and how to fix
- Git automatically changes the End Of Line (EOL) Sequence of some files from LF to CRLF, causing problems with docker
    - Fix: after cloning the repo, manually change the EOL sequence of the following files to LF instead of CRLF:
        - docker\backend\Dockerfile
        - docker\backend\wsgi-entrypoint.sh
        - docker\nginx\Dockerfile 

# BY:
- MUHAMMAD ZYAD ZARIN BIN ZAMBERI
- MICHELLE LOH
- NUR ’AQILAH BINTI FAKHRURRAZI
