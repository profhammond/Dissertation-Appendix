# Dissertation Appendix

Supporting material for Scott G. Hammond’s dissertation, *Developing and Evaluating a Reliable Deep Learning Framework for Melanoma Classification*.

Intended repository: https://github.com/profhammond/Dissertation-Appendix

## Contents

- `supplementary/tables/`: LaTeX tables referenced by Appendix Q.
- `supplementary/figures/`: supplementary numerical plots referenced by Q.
- `historical/appendix_q_source.tex`: unchanged staging source, excluded from the dissertation build.
- `docs/`: migration decisions and evidence limitations.
- `provenance/`: dependency inventory, source hash and package checksums.
- `scripts/verify_package.py`: standard-library checksum verification.

Start with [the documentation guide](docs/README.md) and [the review](docs/reproducibility_review.md). This is a supplementary archive, not a complete experimental reproduction environment. No models, source medical images, numerical heatmaps or datasets are included. Qualitative galleries and conflicting historical training instructions are not promoted to verified documentation.

## Evidence status

Formula recalculation, table aggregation, saved-map metric reproduction, baseline configuration and model-generation identity require separate evidence. A checksum establishes byte identity only. The four-method recorded-pair protocol audit is still pending review at this checkpoint. Existing audits saved by the author in GitHub are not overwritten or incorporated automatically by this package.

## Use

Extract this ZIP, open its `Dissertation-Appendix` folder, and upload the contents to the repository root. Preserve existing audit folders and README content when merging. Run `python scripts/verify_package.py` locally or in Colab after obtaining the repository. The historical LaTeX staging source is not a standalone document and has deliberately withheld image dependencies.

## Rights and availability

No license is assigned by this package. Dataset-provider rights remain applicable to underlying research data. This archive does not claim independent retraining, model inference, attribution generation or full historical environment reproduction.
