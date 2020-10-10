# cds-hooks-work
*cds-hooks-work* is a framework for creating clinical decision support services in python. It implements the models and workflows specified by [HL7 CDS HOOKS](https://cds-hooks.hl7.org/). 

### Usage
General usage of `cds-hooks-works` includes creating an `App` model and registering one or more `Service` models. Each service model takes a handler in which you implement your cds-hook logic. This can be registered manually or conveniently through decorators as demonstrated below. The framework comes packaged with `Flask` for running your webservice, or bring your own webserver and utilize `cds-hooks-work` for it's typed models and cds-hook flow abstraction.   

```python
import cds_hooks_work as cds
import os

app = cds.App()


@app.patient_view("patient-greeting", "The patient greeting service greets a patient!", title="Patient Greeter")
def greeting(r: cds.PatientViewRequest, response: cds.Response) -> cds.Response:
    response.cards = [cds.Card.info("hello world!", "demo_service")]
    response.httpStatusCode = 200


if __name__ == '__main__':
    debug = os.environ.get('DEBUG', False)
    port = os.environ.get("PORT", 5000)
    app.serv(host="0.0.0.0", debug=debug, port=port)

```


