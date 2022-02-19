#!/usr/bin/env python3

# DEPENDENCIES:
#    pip3 install pyqt5


import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

SAMPLES = {
    8: "It is not a lack of love, but a lack of friendship that makes unhappy marriages. And those who were seen dancing were thought to be insane by those who could not hear the music.  <i>― Friedrich Nietzsche</i>",
    16: "Whoever fights monsters should see to it that in the process he does not become a monster. And if you gaze long enough into an abyss, the abyss will gaze back into you. The individual has always had to struggle to keep from being overwhelmed by the tribe. If you try it, you will be lonely often, and sometimes frightened. But no price is too high to pay for the privilege of owning yourself. <i>― Friedrich Nietzsche</i>",
    20: "走為上策",
    24: 'Without music, life would be a mistake. <i>― Friedrich Nietzsche</i>',
}

OUTPUT_FILE = 'fontlistqt.html'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    families = QFontDatabase().families()

    with open(OUTPUT_FILE, mode="w", encoding="utf8") as out:

        print('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
    p span {
        color: #ccc;
        }

        p {
            line-height: 160%;
            margin: 1em 20%;
        }

        ul {
            list-style-type: none;
            /* line-height: 160%;
            margin: 3em 20%; */
        }

        h1 {
            padding: 1.5em 0 0.5em 0;
            margin: 0;
            text-align: center;
            box-sizing: border-box;
            color: black;
            font-size: 35pt;
            text-shadow: rgb(51 49 42 / 40%) 1px 0px 5px;
        }

        body,
        body>div.center.rounded {
            min-height: 96%;
        }

        .center {
            display: flex;
            width: auto;
            flex-direction: column;

            /* height: 95vh; */
            justify-content: center;
            align-items: center;
        }

        hr {
            border: 1px dotted #ccc;
        }

        .rounded {
            -webkit-box-shadow: rgb(29 36 23 / 39%) -2px 4px 17px 0px;
            -moz-box-shadow: rgba(29, 36, 23, 0.386719) -2px 4px 17px 0px;
            box-shadow: rgb(29 36 23 / 39%) -2px 4px 17px 0px;
            padding: 20px;
            -webkit-border-radius: 11px;
            -moz-border-radius: 11px;
            border-radius: 11px;
        }

        @media (max-width: 600px) {

            .center {
                display: flex;
                /* height: 98vh; */
                justify-content: center;
                align-items: center;
            }

            .centered {
                text-align: center;
            }

            p {
                line-height: 150%;
                margin: 0.4em;
            }

            h1 {
                text-align: center;
                box-sizing: border-box;
                font-family: inherit;
                margin: .5em;
                font-weight: bold;
                line-height: 140%;
                color: gray;
                font-size: 25pt;
            }

            .rounded {
                -moz-box-shadow: none;
                -webkit-box-shadow: none;
                box-shadow: none;
                border: 0;
                -webkit-border-radius: 0;
                -moz-border-radius: 0;
                border-radius: 0;
            }
        }
    </style>
</head>

<body>
    <div class="center rounded">
    <ul>
    ''', file=out)
        print(f'<li>Total fonts: {len(families)}</li>', file=out)

        for family in sorted(families):
            print(f'''
      <li>
        <h1 style="font-family:'{family}'">
            {family}
        </h1>''', file=out)

            for font_size_pt, paragraph in SAMPLES.items():
                print(f'''
                <p style="font-family:'{family}'; font-size:{font_size_pt}pt;">
                    <span>{font_size_pt}pt:</span> {paragraph}
                </p>''', file=out)
            print('''
       </li>
    ''', file=out)

        print('''
        </ul>
        </div>
        </body>
        </html>
        ''', file=out)
    print(f'Wrote file {OUTPUT_FILE}')
