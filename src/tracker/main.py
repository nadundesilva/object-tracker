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
import cv2


def cli():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        typer.echo("Unable to open camera")
        typer.Exit(1)

    ok, frame = cap.read()
    if not ok:
        typer.echo("Unable to read initial frame from camera")
        typer.Exit(1)

    height = frame.shape[1]
    width = frame.shape[1]
    typer.echo(
        "Started tracking video of size ({height}, {width})".format(
            height=height, width=width
        )
    )

    while True:
        ok, frame = cap.read()
        if not ok:
            typer.echo("Unable to read frame from camera")
            break

        frame = cv2.flip(frame, 1)
        x1 = int(height / 3)
        y1 = int(width / 3)
        cv2.rectangle(frame, (x1, y1), (x1 * 2, y1 * 2), (0, 255, 0), 2)
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
