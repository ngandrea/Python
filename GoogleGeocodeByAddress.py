from temboo.Library.Google.Geocoding import GeocodeByAddress
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("ngandrea", "myFirstApp", "1d24c665d3394db49ed936e8853585d0")

# Instantiate the Choreo
geocodeByAddressChoreo = GeocodeByAddress(session)

# Get an InputSet object for the Choreo
geocodeByAddressInputs = geocodeByAddressChoreo.new_input_set()

# Set the Choreo inputs
geocodeByAddressInputs.set_Address("21 Tampines Ave 1, 529757")

# Execute the Choreo
geocodeByAddressResults = geocodeByAddressChoreo.execute_with_results(geocodeByAddressInputs)

# Print the Choreo outputs
print("Latitude: " + geocodeByAddressResults.get_Latitude())
print("Response: " + geocodeByAddressResults.get_Response())
print("Longitude: " + geocodeByAddressResults.get_Longitude())