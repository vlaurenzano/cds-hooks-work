import unittest
from cds_hooks_work.request import *  # its a test
from cds_hooks_work.response import *
from cds_hooks_work.service import *
import json

patient_view_stub_json = r'{"context": {"patientId": "smart-1288992", "userId": "Practitioner/COREPRACTITIONER1"}, "fhirServer": "https: //launch.smarthealthit.org/v/r2/fhir", "hook": "patient-view", "hookInstance": "d4fc8092-6a7f-47f1-aa58-fc158368c11c", "prefetch": {"patient": {"active": true, "address": [{"city": "Tulsa", "country": "USA", "line": ["1HillAveApt14"], "postalCode": "74117", "state": "OK", "use": "home"}], "birthDate": "1925-12-23", "gender": "male", "id": "smart-1288992", "identifier": [{"system": "http: //hospital.smarthealthit.org", "type": {"coding": [{"code": "MR", "display": "Medicalrecordnumber", "system": "http: //hl7.org/fhir/v2/0203"}], "text": "Medicalrecordnumber"}, "use": "usual", "value": "1288992"}], "meta": {"lastUpdated": "2020-10-07T02: 30: 20.221-04: 00", "tag": [{"code": "smart-8-2017", "system": "https: //smarthealthit.org/tags"}], "versionId": "578"}, "name": [{"family": ["Adams"], "given": ["Daniel", "X."], "use": "official"}], "resourceType": "Patient", "telecom": [{"system": "email", "value": "daniel.adams@example.com"}], "text": {"div": "<divxmlns=\"http: //www.w3.org/1999/xhtml\"><p>DanielAdams</p></div>", "status": "generated"}}}}'


class PatientViewModelTest(unittest.TestCase):
    def test_hydrate_patient_vew(self):
        patient_view_stub = json.loads(patient_view_stub_json)
        patientView = PatientView(patient_view_stub)
        self.assertIsInstance(patientView.context, PatientViwContext)
        self.assertEqual(patientView.context.patientId, "smart-1288992")


class ResponseTest(unittest.TestCase):
    def test_cards(self):
        c = Card.info("bla", "bla", suggestions="dfdf")


class ServicesTest(unittest.TestCase):
    def test_serialize(self):
        service = Service("hook", "id", "desc")
        services = Services()
        services.register_service(service)
        d = services.to_dict()
        j = json.dumps(d)
        self.assertEqual(
            '{"services": {"hook": "hook", "id": "id", "description": "desc", "title": "", "prefetch": ""}}', j)


if __name__ == '__main__':
    unittest.main()
