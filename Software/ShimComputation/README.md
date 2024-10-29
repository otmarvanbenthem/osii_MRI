# Shim Optimization

## Inputs

### Magnet Positions - `mag_pos_fname`

CSV with positions of potential magnets positions in the following format:

| X   | Y   | Z   |
|-----|-----|-----|
| x_0 | y_0 | z_0 |
| x_1 | y_1 | z_1 |

### B0 Map - `b0_map_fname`

CSV with B0 field map in the following format:

| X   | Y   | Z   | B_0  |
|-----|-----|-----|------|
| x_0 | y_0 | z_0 | B0_0 |
| x_1 | y_1 | z_1 | B0_1 |

B0 is in T

## Outputs

### Optimal Shim - `shim_out.csv`

CSV specifying whether a magnet should be placed at each position, and if so, at what angle.

| X   | Y   | Z   | Place   | Angle   |
|-----|-----|-----|---------|---------|
| x_0 | y_0 | z_0 | place_0 | angle_0 |
| x_1 | y_1 | z_1 | place_1 | angle_1 |

Place is True or False

### Optimization result - `optimization_results.pickle`

Pickle file with all optimization results. For more detail on what this includes, please consult the [pymoo documentation](https://pymoo.org/interface/result.html?highlight=results).