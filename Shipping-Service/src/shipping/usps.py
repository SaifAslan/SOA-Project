from shipping.address import Address
from shipping.package import Package
from shipping.base import CourierTracker, InvalidTrackingNumber, TrackingResult, \
                          TrackingCheckpoint, format_timestamp
from requests import get
from string import digits
from bs4 import BeautifulSoup
from datetime import datetime

class USPSTracker(CourierTracker):
    """Tracker object for Speedex tracking numbers`"""
    # RE for matching service methods

    # Initialization of a new port office
    def __init__(self):
        # Call super
        username = "example"
        # Production URL
        self.tracking_endpoint = 'http://production.shippingapis.com/ShippingAPI.dll?API=TrackV2&XML=' + \
            '<TrackFieldRequest USERID="{username}">' + \
                '<TrackID ID="{tracking_id}"></TrackID>' + \
            '</TrackFieldRequest>'
        self.address_validation_endpoint = 'http://production.shippingapis.com/ShippingAPI.dll?API=Verify&XML=' + \
            '<AddressValidateRequest USERID="{username}">' + \
                '<IncludeOptionalElements>true</IncludeOptionalElements>' + \
                '<ReturnCarrierRoute>true</ReturnCarrierRoute>' + \
                '<Address ID="0">' + \
                    '<FirmName>{name}</FirmName>' + \
                    '<Address1>{address_1}</Address1>' + \
                    '<Address2>{address_2}</Address2>' + \
                    '<City>{city}</City>' + \
                    '<State>{state}</State>' + \
                    '<Zip5>{zip5}</Zip5>' + \
                    '<Zip4>{zip4}</Zip4>' + \
                '</Address>' + \
            '</AddressValidateRequest>'
        self._base_rate_endpoint = 'http://production.shippingapis.com/ShippingAPI.dll?API={api}&XML=' + \
          '<{api}Request USERID="{{username}}">' + \
                '<Revision>2</Revision>' + \
                '{{package}}' + \
            '</{api}Request>'
        self.domestic_rate_endpoint = self._base_rate_endpoint.format(api='RateV4')
        self.international_rate_endpoint = self._base_rate_endpoint.format(api='IntlRateV2')


    def sanitize(self, tracking_number: str) -> str:
        '''Attempts to sanitize the given tracking number according to Speedex format'''
        new = ''.join([i for i in str(tracking_number) if i in self.allowed])
        if len(new) != 12:
            raise InvalidTrackingNumber(
                message='Speedex Tracking Numbers must contain 12 digits.')
        return new

    def fetch_results(self, tracking_number: str) -> BeautifulSoup:
        '''Requests tracking information for the given tracking number'''
        results = BeautifulSoup(
            get(self.base_url+str(tracking_number)).text, features="html.parser")
        self.last_tracked = tracking_number
        return results

    def parse_results(self, tracking_info: BeautifulSoup) -> dict:
        '''Parses the results into useable  information'''

        def parse_checkpoint(checkpoint: BeautifulSoup):
            items = checkpoint.find("span", {"class": "font-small-3"}).contents[0].split(", ")
            timestamp = datetime.strptime(items[1], "%d/%m/%Y %H:%M")
            date = items[1]
            location = items[0]
            description = checkpoint.find("h4", {"class": "card-title"}).contents[0].text

            return TrackingCheckpoint(description, date, location, format_timestamp(timestamp))

        tracking_number = tracking_info.find(attrs={"id": "TxtConsignmentNumber"}).get('value')

        if tracking_info.find("div", {"class": "alert-warning"}):
            return TrackingResult('Speedex', tracking_number, [], False)

        package = tracking_info.find_all("div", {"class": "timeline-card"})
        delivered = package[-1].find("h4", {"class": "card-title"}).contents[0].text == "Η ΑΠΟΣΤΟΛΗ ΠΑΡΑΔΟΘΗΚΕ"
        updates = [parse_checkpoint(update) for update in package]
        return TrackingResult('Speedex', tracking_number, updates, delivered)


    def track(self, tracking_number: str):
         # Compose the URL formatting parameters
        params = {
            'tracking_id': tracking_number
        }

        # Make a request for the event-level information
        raw_response = super(USPSTracker, self).get_server_response(self.tracking_endpoint, params, method='Tracking')

        # Extract the XML data from the parsed response
        track_info = raw_response.find('TrackInfo')

        # Check to see if we got a valid response
        error = track_info.find('Error')
        if error is not None:
            return self.process_exception(error)

        # Current event/summary
        raw_events = [track_info.find('TrackSummary')]
        # Remaining past events
        raw_events.extend(track_info.findall('TrackDetail'))

        # Create the TrackingResponse and TrackingEvents
        response = TrackingResult('USPS', tracking_number, [], [])
        # for event in raw_events:
        #     response.add(
        #         TrackingEvent(
        #             event.find('EventState').text or 'NONE',
        #             event.find('EventCity').text or 'NONE',
        #             event.find('EventZIPCode').text,
        #             event.find('Event').text,
        #             event.find('EventDate').text or 'January 01, 1970',
        #             event.find('EventTime').text or '12:00 am',
        #             date_format='%B %d, %Y',
        #             time_format='%I:%M %p'
        #         )
        #     )

        return response

    def track_silently(self, tracking_number: str):
        return self.track(tracking_number)
        
    def calculate_cost(self, source: Address, target: Address, package: Package):
        return 450.43