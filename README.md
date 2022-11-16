# Activity Recognition

* Write an abstract and put a nice picture here.

> To evalute the best model, please visit the presentation notebook [here](./notebooks/presentation.ipynb).

## Benchmarks

* Put a table listing of the benchmarks comparing all our models and other models for reference.
<img src='./assets/benchmarks.png' width=800 />

## Visuals

* Put sample prediction from model, maybe one of each class (3x3 grid).
<img src='./assets/visuals.png' widht=800 />

## Organisation

```txt
.
|-- assets              # contains presentation images,documents etc. 
|-- data                # contains raw/splits data.
|-- models              # contains model definitions.
|-- notebooks           # contains related notebooks.
    |-- explorations    # notebook for exploring data.
    |-- presentation    # notebook that presents the final model.
    |-- validations     # notebook to validate and understand model output.
|-- utils               # contains common utilities used by models.
    |-- datasets.py     # dataset definitions and transformations.
    |-- metrics.py      # metrics used for performance measurement.
|-- README.md           # you're reading this :)
```

## Models

*List of models we tried, with their performance and flaws.*

* CNN with Bidirectional LSTMs ([model](./models/cnn_lstm))

Write something about this here.

* Recurrent Neural Networks ([model](./models/rnn))

Write something about this here.

* 1D Convolutional Network ([model](./models/1d_conv/))

Write something about this here.
