# Conda Setup

The dependencies of this package are managed using conda. 
Before using this package, make sure that you have installed conda. 
Installation instructions can be found at the link below:

https://docs.conda.io/projects/conda/en/latest/user-guide/install/

Before activating the env, make sure that you have exported your default
`PATH` variable to your conda installation. It is advised to create a
function in your `.bashrc` to quickly switch between `PATH` variables, 
especially when developing this package. Sample bash commands used to activate
and deactivate conda are included below (assuming conda has been installed
under `/home/user/`):

#### Change to conda env

```{bash}
$ export ORIGINAL_PATH=$PATH
$ export PATH="/home/user/miniconda3/bin:$PATH"
```

#### Restore original env
```{bash}
$ export PATH=$MY_ORIGINAL_PATH
```

Note that any active conda environments must be deactivated prior to restoring
your original environment.

# Environment Setup

To set up the `env_f1_stats` environment needed to run this package, you can
set up the environment using the `env_f1_stats.yml` config file in the top
level of this repository. The bash command is included below:

```{bash}
$ conda env create -f env_f1_stats.yml
```

To add or remove dependencies from the envrionment, edit `env_f1_stats.yml`
and rebuild the environment using the command below:

```{bash}
$ conda env update --prefix ./env_f1_stats --file env_f1_stats.yml  --prune
```

# Environment Activation

Commands used to activate and deactivate the conda environment are found
below:

#### Activate `env_f1_stats`

```{bash}
$ conda activate ./env_f1_stats
```

or

```{bash}
$ source activate env_f1_stats
```

#### Deactivate `env_f1_stats`
```{bash}
$ conda deactivate
```

or

```{bash}
$ source deactivate
```
