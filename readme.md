# Cheverto-Uploader

Upload image to [cheverto](https://chevereto.com/), an image hosting software. Only supporting dashboard V3 so far.

## Installation

```shell
git clone git@github.com:KARLSZP/Chevereto-Uploader.git
pip install requests
pip install yaml
```

## Initialization

### Retrieve the API Key

1. Go to `https://[site]/dashboard/settings/api`.
2. Login and get your `API Key`.

### Config From command line

```
python upload.py init
```

### Create `config.yml`[optional]

Create new config file `config.yml` in the same directory.

```yaml
USER_CFG:
  BASE_URL: https://[site]
  KEY: [API Key]
```

### Config Typora

`File` - `Preferences...` - `Image`

and do as follow:

<img src="https://img.karlszp.club/images/2023/06/13/image-20230613012728724.png" alt="image-20230613012728724" style="zoom:67%;" />

Once the test passed, you can paste images into Typora and find them **automatically** uploaded.



## TODOs

1. Adapt to Cheverto V4 API
2. Python-free versions with shell scripts



---

2023-06-13 karlzpsong