# Calculating Jet Emissions of the Ultra-Wealthy

### Project Collaborators: Jason Dahl, Sophia McConnell

## Description

The goal of this project is to raise awareness of the level of carbon emissions emitted by ultra-wealthy individuals, with the ultimate goal of discouraging such emission-intensive behavior. This will be accomplished by scheduling automated collection of data from publicly available flight logs of wealthy individuals, feeding that data through a calculator, and posting to a social media account a record of the amount of carbon emitted into the atmosphere.

A “nice-to-have” bit of additional functionality would include a comparison to a more relatable form of carbon emission. An example social media post might read: “Warren Buffet just put 45 tons of CO2 into the atmosphere flying from Omaha to Nashville. That’s the equivalent of driving from Los Angeles to New York 3 times.”

## Docker Instructions

In the root directory, run `docker build .`.

Then run `docker images` and copy the ID of the image you've just created.

Finally, run `docker run -it --mount type=bind,source=${PWD},target=/project IMAGEID_GOES_HERE bash` to create the container.

This will bind your local /app directory with the /app directory in the container.
