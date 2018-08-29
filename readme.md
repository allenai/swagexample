SWAG Example
============
An example model for the [SWAG leaderboard][swag-leaderboard].

This repo demonstrates how to make a submission to the SWAG leaderboard
using [allennlp][allennlp]. The model is fairly simple and doesn't
actually achieve much better than random chance due to SWAG being
difficult for language models by design.


Setup
-----
First, you'll need [docker][docker] and [python 3.6][python]
installed. [pyenv][pyenv] and [pyenv-virtualenv][pyenv-virtualenv] can
be helpful for managing python versions and environments. Once you've
installed python 3.6, run:

    pip install --editable .

In order to make a submission to the leaderboard, you'll also need to
[sign up for beaker][beaker].


Quickstart
----------
This submission example is built with [allennlp][allennlp]. Allennlp
makes available a command line interface you can use to train, predict
with, and evaluate your models:

    allennlp --help

Optionally, you can download the SWAG [train][train-data] and
[dev][dev-data] data. The SWAG dataset reader in this repo handles
downloading the data automatically when you run training, so you don't
have to download it manually.

To make a submission, you should train the model (which could take
several hours). The following command trains the model that ships with
this repo, saving the parameters to the [`models/`](./models/)
directory:

    allennlp train configs/model.json           \
      --serialization-dir models/swagexample-v1 \
      --include-package swagexample

See `allennlp train --help` for details on the command and its options.

Once the model is trained, you can package the model up into a docker
container:

    sudo docker build --tag swagexample .

Upload that image to a beaker blueprint:

    sudo beaker blueprint create --name swagexample swagexample

And then submit the example for evaluation on the dev set on the
leaderboard [here][swag-submissions].


Contributing
------------
Feel free to file an issue on the [github repository][swagexample-repo].


[allennlp]: https://allennlp.org
[beaker]: https://beaker.allenai.org
[docker]: https://docker.com
[pyenv]: https://github.com/pyenv/pyenv
[pyenv-virtualenv]: https://github.com/pyenv/pyenv-virtualenv
[python]: https://python.org
[swag-leaderboard]: https://leaderboard.allenai.org/
[swag-submissions]: https://leaderboard.allenai.org/submissions
[swagexample-repo]: https://github.com/allenai/swagexample
[train-data]: https://storage.googleapis.com/ai2-leaderboard/swag-train.csv
[dev-data]: https://storage.googleapis.com/ai2-leaderboard/swag-dev.csv
