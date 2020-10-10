# cds-hooks-work
*cds-hooks-work* is a framework for creating clinical decision support services in python. It implements the models and workflows specified by [HL7 CDS HOOKS](https://cds-hooks.hl7.org/). 

### Usage
General usage of `cds-hooks-works` includes creating an `App` model and registering one or more `Service` models. Each service model takes a handler in which you implement your cds-hook logic. The framework comes packaged with `Flask` for running your webservice, simply pass the `App` model to the `serve` function, or bring your own webserver and utilize `cds-hooks-work` for it's typed models and cds-hook flow abstraction.   

```python
import cds_hooks_work as cds

app = cds.App()

def greeting(r: cds.PatientViewRequest) -> cds.Response:
    resp = cds.Response()
    resp.cards = [cds.Card.info("hello world!", "demo_service")]
    return resp


service = cds.Service.patient_view("myid", "mydesc", greeting)

app.register_service(service)

cds.serve(app, debug=True)

```


