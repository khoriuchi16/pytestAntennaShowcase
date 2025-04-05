# pytestAntennaShowcase
Repository to showcase pytest's ability automate testing for a hypothetical antenna system


## Download dependencies
pip install -r requirements.txt

## To run test suite
pytest -s


## Ways to induce failure in test_antenna.py
Line 20: connection_interface.write(b'OTA_AUTH admin pass123\n') => change the username/password to something incorrect

Line 92: time.sleep(2) => induces failure if > 3 seconds

Line 118: current_position = current_position + 0.5 => some pertubuation or error; induces failure if > 1 degree
