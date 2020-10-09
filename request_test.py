import unittest
from request import * #its a test

patient_view_stub = {"context": {"patientId": "smart-1288992","userId": "Practitioner/COREPRACTITIONER1"}, "fhirServer": "https: //launch.smarthealthit.org/v/r2/fhir","hook": "patient-view","hookInstance": "d4fc8092-6a7f-47f1-aa58-fc158368c11c","prefetch": {"patient": {"active": True,"address": [{"city": "Tulsa","country": "USA","line": ["1HillAveApt14"],"postalCode": "74117","state": "OK","use": "home"}],"birthDate": "1925-12-23","gender": "male","id": "smart-1288992","identifier": [{"system": "http: //hospital.smarthealthit.org","type": {"coding": [{"code": "MR","display": "Medicalrecordnumber","system": "http: //hl7.org/fhir/v2/0203"}],"text": "Medicalrecordnumber"},"use": "usual","value": "1288992"}],"meta": {"lastUpdated": "2020-10-07T02: 30: 20.221-04: 00","tag": [{"code": "smart-8-2017","system": "https: //smarthealthit.org/tags"}],"versionId": "578"},"name": [{"family": ["Adams"],"given": ["Daniel","X."],"use": "official"}],"resourceType": "Patient","telecom": [{"system": "email","value": "daniel.adams@example.com"}],"text": {"div": "<divxmlns=\"http: //www.w3.org/1999/xhtml\"><p>DanielAdams</p></div>","status": "generated"}}}}


class RequestModelHydrate(unittest.TestCase):
    def test_hydrate_patient_vew(self):
        patientView = PatientView(patient_view_stub)
        self.assertIsInstance(patientView.context, PatientViwContext)
        self.assertEqual(patientView.context.patientId, "smart-1288992")


if __name__ == '__main__':
    unittest.main()
