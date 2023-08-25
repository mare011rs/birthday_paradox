## The Birthday paradox

The [Birthday paradox](https://en.wikipedia.org/wiki/Birthday_problem#:~:text=The%20birthday%20paradox%20refers%20to%20the%20counterintuitive%20fact%20that%20only%2023%20people%20are%20needed%20for%20that%20probability%20to%20exceed%2050%25.) refers to the counterintuitive fact that only 23 people are needed for probability of a matching birthday between them to exceed 50%.

We intuitively think that because there are 365 days in the year we would need half of that number to achieve the 50% chance of matching birthdays, but the trick is that everybody is being compared with everybody and we are checking for matches between each person. This quickly increases the number of comparisons by each person added to the group, increasing the probability of a match.

## How to run
1. Download [Docker desktop](https://www.docker.com/products/docker-desktop/), install it on your computer and run it.
2. Run the following commands 
```bash
git clone https://github.com/mare011rs/birthday_paradox.git
cd birthday_paradox
docker build -t birthday_paradox .
docker run -p 5001:5001 birthday_paradox
```
3. Run `http://localhost:5001/` in your browser.