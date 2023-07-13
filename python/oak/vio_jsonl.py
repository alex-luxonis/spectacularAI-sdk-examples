import depthai
import spectacularAI
import time

pipeline = depthai.Pipeline()

#vio_pipeline = spectacularAI.depthai.Pipeline(pipeline)
config = spectacularAI.depthai.Configuration()
config.ensureSufficientUsbSpeed = False
vio_pipeline = spectacularAI.depthai.Pipeline(pipeline, config)

with depthai.Device(pipeline) as device, \
    vio_pipeline.startSession(device) as vio_session:

    while True:
        out = vio_session.waitForOutput()
        print(out.asJson())
