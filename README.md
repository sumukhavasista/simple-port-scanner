**Overview**
The Simple Port Scanner is a web-based tool built using Flask and Nmap that allows users to scan open ports on a specified target IP address. This project aims to help users understand networking basics, including port numbers and services, and provides a foundation for expanding the tool to include vulnerability scanning features.

**Features**
Scan for open ports on a target IP address.
Display scan results in a user-friendly web interface.
Show details for each open port, including port number, service, and version information.
Easy to use with minimal setup.

**Technologies Used**
Flask: A lightweight web framework for Python.
Nmap: A powerful network scanning tool used to discover hosts and services on a network.
HTML/CSS: For creating the web interface.
Python: The programming language used for backend logic.

**Installation**
Clone the repository: [port-scanner] (git remote add origin [https://github.com/sumukhavasista/port-scanner.git](https://github.com/sumukhavasista/simple-port-scanner.git))
cd simple-port-scanner



python -m venv venv
source venv/bin/activate  On Windows use `venv\Scripts\activate` 

*Required packages*
`pip install Flask python-nmap`

**Usage**
Open your web browser and navigate to http://localhost:5000.
Enter the IP address you want to scan in the input field and click "Scan."
The results will be displayed on a new page, showing all open ports and their associated service details.

To run the application , execute the following command in your terminal:
`python app.py`

>Scanning Remote IP Addresses
To scan a remote IP address, simply enter the target's IP in the input field.
Ensure you have permission to scan the target system.

>Legal and Ethical Considerations
<IMPORTANT: Always obtain explicit permission from the owner of the target system before conducting any scans. Unauthorized scanning may be illegal and could lead to severe consequences.

>Future Improvements
Implement vulnerability scanning features based on the open ports.
Add user authentication for tracking previous scans.
Improve the UI for better user experience.
Include more detailed output, such as device type and operating system detection.

**LICENSE**
This project is licensed under MIT
