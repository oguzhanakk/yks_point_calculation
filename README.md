# yks_point_calculation

Score calculation backend service for the KolayHedef mobile app.

This project is used to calculate the TYT and AYT exam scores in Turkey's university entrance exams. It is developed using the Flask web framework.

## Getting Started

You can start by cloning the project to your computer.

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the project to your computer:

git clone https://github.com/KolayHedef/KolayHedefParser.git


2. Create a virtual environment and activate it:

python3 -m venv myprojectenv source myprojectenv/bin/activate


3. Install the required packages:

pip install Flask


4. Run the application:

python app.py


Now your application should be running at `http://localhost:5000`.

## API Usage

You can use the following API endpoint for score calculation:

POST /puan_hesapla


Example JSON request body:

```json
{
    "obp": 50,
    "tr_net": 30,
    "sosyal_net": 15,
    "mat1_net": 25,
    "fen_net": 20,
    "mat2_net": 10,
    "fizik_net": 5,
    "kimya_net": 6,
    "biyo_net": 7,
    "edb_net": 8,
    "tarih1_net": 4,
    "cog1_net": 3,
    "tarih2_net": 9,
    "cog2_net": 10,
    "felsefe_net": 11,
    "din_net": 12,
    "dil_net": 60
}
License
This project is licensed under the MIT License - see the LICENSE file for details.