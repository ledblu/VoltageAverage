import numpy as np   
import math

from saleae.range_measurements import AnalogMeasurer


class voltage_average_meas(AnalogMeasurer):
    supported_measurements = ['avg']

    def __init__(self, requested_measurements):
        super().__init__(requested_measurements)

        self.requested_measurements = requested_measurements
        self._sum = 0.0
        self._sample_count = 0

    def process_data(self, data):
        if data.sample_count == 0:
            return

        self._sum += np.sum(
            data.samples,
            dtype=np.float64
        )

        self._sample_count += data.sample_count

    def measure(self):
        values = {}

        if 'avg' in self.requested_measurements:
            if self._sample_count == 0:
                values['avg'] = float("nan")
            else:
                values['avg'] =  self._sum / self._sample_count
                

        return values
