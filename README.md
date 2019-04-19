# oppaipy

oppaipy is a simple object-oriented python3 wrapper around the python bindings of [oppai-ng](https://github.com/Francesco149/oppai-ng).

## Usage
```
$ pip install oppaipy
```

There are 5 steps to using oppaipy:

1. Initialise
2. Set parameters
3. Calculate
4. Check results
5. Release resources

### Example
```python
>>> import oppaipy
>>> calc = oppaipy.Calculator()
>>> calc.set_beatmap("/path/to/beatmap")
>>> calc.set_misses(1)
>>> calc.calculate()
>>> print(calc.pp)
727.3976135253906
>>> calc.close()
```

There is some extra syntactic sugar to make it shorter for simple usage however

### Simple example
```python
>>> import oppaipy
>>> with oppaipy.Calculator("/path/to/beatmap", misses=1) as calc:
...     print(calc.calculate())
(7.8976135253906, 727.3976135253906)
```

## API
```python
# Setting parameters
Calculator.set_beatmap(beatmap_path)
Calculator.set_mods(mods)
Calculator.set_combo(combo)
Calculator.set_accuracy_percent(accuracy)
Calculator.set_accuracy(count_100, count_50)
Calculator.set_misses(misses)
Calculator.set_score_version(score_version)
Calculator.set_base_ar(ar)
Calculator.set_base_od(od)
Calculator.set_base_cs(cs)
Calculator.set_base_hp(hp)
Calculator.reset()

# Calculating
Calculator.calculate()

# Getting values
Calculator.pp
Calculator.aim_pp
Calculator.speed_pp
Calculator.acc_pp
Calculator.stars
Calculator.aim_stars
Calculator.speed_stars

# Cleanup
Calculator.close()
```

## Why should I use this?
You get the speed of the C bindings with a pythonic object interface.

## Why the name "oppaipy"?
I already used "OOppai" for [the wrapper of the original oppai's bindings](https://github.com/Syriiin/OOppai), and I didn't like the look of "OOppai-ng".
