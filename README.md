# Surfs Up

## Overview of Weather Analysis
### Purpose
The purpose of this analysis was to gather data from weather stations in Hawaii to determine viability of a new ice cream and surf shop business. In order to determine if the surf shop is viable all year, I examined the historic weather data from the months of June and December.

## Results
### Key Differences Between June and December Weather Data
- The average temperature in June, 74.9 °F, is slightly higher than the average temperature in December, 71.0 °F.
- The minimum temperature in June, 64.0 °F, is considerably higher than the minimum temperature in December, 56.0 °F.
- The maximum temperature in June, 85.0 °F, is slightly higher than the maximum temperature in December, 83.0 °F.
- The standard deviation of the June data, 3.3, and the range, 21.0 °F, are both lower than the standard deviation, 3.7, and the range, 27.0 °F of the December data. Therefore the temperature in December varies more on average than in June.

## Summary
### Biggest Takeaways
The analysis shows that the average and maximum temperatures in June are only slightly higher than those temperatures in December, while the minimum temperatures in June are considerably higher than in December. Since the minimum temperatures will occur at night and the average temperatures for both are in the 70s, it is reasonable to conclude that the location will be warm enough for our shop to succeed at any point in the year.

### Additional Queries
1. I also performed a query of the measurement table to retrieve precipitaion data for the month of June, and then created summary statistics for the average total rainfall in June. (I multiplied the average daily rainfall by 30 to get the average total rainfall.)
```python
june_prcp = session.query(Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
```


2. Similarly, I performed a query of the measurement table to retrieve precipitation data for the month of December, and then created summary statistics for the average total rainfall in December. (I multiplied the average daily rainfall by 31 to get the average total rainfall.)
```python
dec_prcp = session.query(Measurement.prcp).filter(extract('month', Measurement.date)==12).all()
```

#### Takeaways from Additional Queries
These two queries showed that on average total rainfall in June was 4.1 inches while the average total rainfall in December was 6.7 inches. The high amount of rainfall year-round in Oahu should be a consideration for the opening of the shop. While the temperatures are overall warm, ice cream sales are likely to be diminished by rain. We can consider mitigating options such as lots of indoor seating or outdoor patio umbrellas.