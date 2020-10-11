# cds-hooks-work
*cds-hooks-work* is a framework for creating clinical decision support services in python. It implements the models and workflows specified by [HL7 CDS HOOKS](https://cds-hooks.hl7.org/). 

### Usage
General usage of `cds-hooks-works` includes creating an `App` model and registering one or more `Service` models. Each service model takes a handler in which you implement your cds-hook logic. This can be registered manually or conveniently through decorators as demonstrated below. The framework comes packaged with `Flask` for running your webservice, or bring your own webserver and utilize `cds-hooks-work` for it's typed models and cds-hook flow abstraction.   

```python
import cds_hooks_work as cds
import os

app = cds.App()


@app.patient_view("patient-greeting", "The patient greeting service greets a patient!", title="Patient Greeter")
def greeting(r: cds.PatientViewRequest, response: cds.Response):
    response.cards = [cds.Card.info("hello world!", "demo_service")]
    response.httpStatusCode = 200


if __name__ == '__main__':
    debug = os.environ.get('DEBUG', False)
    port = os.environ.get("PORT", 5000)
    app.serv(host="0.0.0.0", debug=debug, port=port)

```

View the preceeding example in action on the [cds-hooks-sandbox](https://sandbox.cds-hooks.org/?serviceDiscoveryURL=https://test-cds-service.herokuapp.com/cds-services), as implemented by this [demo application](https://github.com/vlaurenzano/cds-hooks-works-example)


### Request Models 

The app unpacks the response from the CDS client according to the specifications given for the particular cds-hook. There is a parent `Request` model that holds all top level values, such as hook, authorization, prefetch. The `Request` model is extended for specific hook types to provide specific `context` models, such as the `PatientViewRequest` model which holds a reference to the `PatientViewContext` model.        

### Response models

The response models are hydrated by the user specified callbacks. There is only one top level `Response` object that contains fields for `Cards and Actions` as well as a status code. The fields for individual cards refer to simple and complex types, implemented according to the [cds-hooks spec](https://cds-hooks.org/specification/current/#http-response).   


### TODO

* The CDS service workflow if fully modeled except for a `feedback` endpoint. This is an endpoint intended for CDS Client (EHRs) to return feedback about whether the card was accepted or ignored.
 
* Prefetch queries must currently be specified as raw dicts, some classes and helper methods would ensure validity and ease of use. 

* The framework captures FHIR authorization values, but has no built in mechanism to use them in an fhir query. Future iterations may include [fhir-py](https://github.com/beda-software/fhir-py) to assist with making fhir queries.      
