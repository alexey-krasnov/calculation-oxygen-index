<h1 align="center">calculation-oxygen-index</h1>
<p>
  <a href="https://twitter.com/AlekseiKrasnov4" target="_blank">
    <img alt="Twitter: AlekseiKrasnov4" src="https://img.shields.io/twitter/follow/AlekseiKrasnov4.svg?style=social" />
  </a>
</p>

> Calculate the oxygen index in non-stoichiometric oxide-based materials according to charge balance rule.

##  Prerequisites

This package requires:

- [pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [chemparse](https://pypi.org/project/chemparse/)


## Usage

### Define a customized compositions data
You should create a `.xlsx` file named `to_predict.xlsx`, in which the compositions that are of interest are listed in the first column with the header "`Initial composition`". There is an example of the `to_predict.xlsx` file in the repository.

### Run the program
After preparing `to_predict.xlsx`, you can calculate oxygen index by two options:
 - 1st option - open `calc_oxygen_index.ipynb` Jupyter lab file and run cell by cell. 
 - 2ns option - run python script `calc_oxygen_index.py`.

It will automatically read `to_predict.xlsx` and make calculation. The results will be stored in files `Revised compositions.csv` and `Revised compositions.xlsx`, where you can find chemical compositions in two columns:
"`Initial composition`" and "`Revised composition`".

## Author

👤 **Aleksei Krasnov**

* Website: [Ph.D. Aleksei Krasnov](https://www.researchgate.net/profile/Aleksei-Krasnov)
* Twitter: [@AlekseiKrasnov4](https://twitter.com/AlekseiKrasnov4)
* Github: [alexey-krasnov](https://github.com/alexey-krasnov)
* LinkedIn: [Aleksei Krasnov](https://linkedin.com/in/aleksei-krasnov-b53b2ab6)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/alexey-krasnov/calculation-oxygen-index/issues). 
