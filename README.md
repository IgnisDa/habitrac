# habitrac

Habitrac is a website that helps you track your habits and keep yourself accountable. You
can access the website [here](https://habitrac.netlify.app/).

The rest of this document will serve as a documentation for the project. You should read it
if you would like to contribute.

## Summary

- [habitrac](#habitrac)
  - [Summary](#summary)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Getting the source code](#getting-the-source-code)
    - [Setup](#setup)
    - [Verification](#verification)
  - [Running the tests](#running-the-tests)
  - [Deployment](#deployment)
    - [Frontend](#frontend)
    - [Backend](#backend)
  - [Built With](#built-with)
  - [Contributing](#contributing)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Others](#others)

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Prerequisites

The main development for Gitzer occurs using [Vagrant](https://www.vagrantup.com/) and all
the associated scripts to setup a development environment for Habitrac are already present in
the repository.

You can install Vagrant from [here](https://www.vagrantup.com/downloads). Once you have
downloaded it, you can verify your installation using `vagrant --version`. At the time of
writing this guide, the output of that command is Vagrant 2.2.14. You might have to restart
your machine after installing Vagrant.

### Getting the source code

You can obtain the source code after you fork habitrac's github
[repository](https://github.com/IgnisDa/habitrac).

```bash
git clone https://github.com/<your-username>/habitrac.git --branch development
```

Development happens primarily on the `development` branch. The website is deployed from the
`main` branch.

### Setup

Once you have verified your installation, you can start the provisioning of the machine
with the following command:

```bash
vagrant up
```

### Verification

If all went well, you should have a functioning development environment now. To verify, run
`vagrant ssh` in the project root. This will directly drop you into a terminal session of the
machine that you just provisioned. Run the following commands to verify if it works
correctly.

```bash
cd ~/habitrac
./tools/run-dev
```

Open up your browser and visit `http://127.0.0.1:8000/` to access the backend development
server powered by Django. Visit `http://127.0.0.1:3000/` to access the frontend development
server powered by NuxtJs.

## Running the tests

This repository has no tests yet. Hopefully, I can fix that in the future. :P

## Deployment

The website is deployed using two platforms: the frontend on
[Netlify](https://habitrac.netlify.app/) and the backend on
[Heroku](https://habitrac.herokuapp.com/). Since this is a mono repository (a repository
that contains all its moving parts/applications in one single git repository), deployment
is a bit tricky.

### Frontend

A custom `netlify.toml` sets some settings to automate this. Simply pushing to the `main` branch
will trigger a deploy.

### Backend

Heroku does not support mono repositories and therefore the changes need to pushed as a
[subtree](https://www.atlassian.com/git/tutorials/git-subtree). A custom configuration using
the file `habitrac/Procfile` handles the rest.

## Built With

- [Contributor Covenant](https://www.contributor-covenant.org/) - Used
  for the Code of Conduct
- [Creative Commons](https://creativecommons.org/) - Used to choose
  the license

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

See also the list of [contributors](contributors.md) who participated in this project.

## License

This project is licensed under the
[Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) - see the
[LICENSE.md](LICENSE.md) file for details

## Others

Project bootstrapped using [cookiecutter](https://github.com/IgnisDa/project-cookiecutter)
by IgnisDa.
