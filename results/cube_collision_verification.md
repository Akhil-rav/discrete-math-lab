# Cube collision audit: execution record

The computation checks the cube incidence bound and capacity identity on the
finite domains below. The [incidence proof](../notes/cube_upper_bound.md)
establishes the bound independently of enumeration.

- All 4,095 nonempty subsets of the twelve cube edges were checked for
  b(B)<=2(|B|-1), with obstruction histograms retained at every size.
- All 174 saved extremizers were checked for avoidance and U+O=1.
- The balances are U=1,O=0 for 150 partitions, and U=0,O=1 for 24, exactly
  symmetry class 7. Representatives have explicit class-matching certificates.
- Tests independently use bit masks for all subsets and color multiplicity
  counters for every saved extremizer. A twelve-color rainbow coloring is a
  negative control; the serialized reference is compared with recomputation.
- All 22 project tests passed. The original dataset, sparse-host dataset,
  and nine-class cube dataset reproduced without changing their results.

## Bounded run

Python 3.13.7 on Windows 11; exact integer arithmetic, no RNG.
Runtime: 0.164701 seconds; status **completed**, exit 0.
Wall limit: 30 seconds; log limit: 1 MiB. No CPU or memory hard limit was
requested. All six declared input hashes were unchanged. Validation passed
against current inputs. The tests were run separately from this recorded audit.

- [Contract](contracts/cube-collisions.json)
- [Manifest](runs/cube-collisions-2026-11-14/manifest.json)
- [Recorded result](runs/cube-collisions-2026-11-14/audit.json)
- [stdout](runs/cube-collisions-2026-11-14/stdout.txt) and
  [stderr](runs/cube-collisions-2026-11-14/stderr.txt)

```sh
python -m experiments.cube_collision_audit --check results/data/cube_collisions.json
python -m unittest discover -s tests -p test_cube_collisions.py -v
```

The recorded output equals the reference byte for byte. The historical
classification record remains intact. The corrected JSON key normalization
was verified before the recorded successful run.

## Interpretation and presentation

The balance identity is proved for all avoiding seven-colorings. The 150/24
counts, class-7 identification, and sharp per-size maxima are finite observations.
The [collision report](cube_collisions.md) records these counts, and the
[four-page cube paper](../papers/cube_classification.pdf) gives the incidence
proof and complete symmetry atlas.
