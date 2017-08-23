# Installation

(Optional but suggested) Create venv for the project

```pip install -r requirements.txt``` 

# Running the REPL application

```python mf-input-client.py repl```

# Features of the REPL

**External to REPL**
Before running a repl, the features of the application can be displayed

```bash 
python mf-input-client.py --help
```

**During REPL**

```bash
> :!help
```

Note: the ! enables external commands, ie commands accessed outside of the REPL

## Exiting the repl

``` > :exit ```