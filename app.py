from flask import Flask, request, render_template
import nmap

app = Flask(__name__)

def nmap_scan(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, arguments='-sV')
    scan_results = []

    for host in nm.all_hosts():
        host_info = {
            'host': host,
            'state': nm[host].state(),
            'ports': []
        }

        for protocol in nm[host].all_protocols():
            ports = nm[host][protocol].keys()
            for port in sorted(ports):
                port_state = nm[host][protocol][port]['state']
                
                if port_state == 'open':
                    port_info = {
                        'port': port,
                        'state': port_state,
                        'service': nm[host][protocol][port]['name'],
                        'version': nm[host][protocol][port].get('version', 'N/A'),
                        'product': nm[host][protocol][port].get('product', 'N/A')
                    }
                    host_info['ports'].append(port_info)

        scan_results.append(host_info)

    return scan_results

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    results = nmap_scan(target)
    return render_template('results.html', results=results, target=target)

if __name__ == "__main__":
    app.run(debug=True)
