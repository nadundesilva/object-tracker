"""Copyright (c) 2021, Deep Net. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import typer
import cv2 as cv


def cli():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        typer.echo("Unable to open camera")
        typer.Exit(1)

    while True:
        frame_read_success, frame = cap.read()
        if not frame_read_success:
            typer.echo("Unable to read frame from camera")
            break

        frame = cv.flip(frame, 1)
        cv.imshow("frame", frame)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()
