Dataset with Lean Manufacturing Tools and Their Commercial Benefits
Source: Figshare
Description: This dataset contains 169 responses to a survey applied to the Mexican maquiladora industry regarding Total Quality Management (TQM), Doing It Right the First Time (DIRFT), wastes, and commercial benefits gained.

    TP – Years of the respondent in the position
    SI – Sector to which it belongs
    GN – Gender
    PE – Position in the Company
    TQM1 – Work teams are available in which various hierarchical levels of the company participate to ensure quality.
    TQM2 – Participatory management is promoted aimed at continuous improvement in all operations.
    TQM3 – The concept of total quality is promoted from raw material collection to after-sales customer service.
    TQM4 – Decision-making for improvement is justified by facts and data.
    TQM5 – The organization focuses on meeting the needs of customers, involving employees to achieve a quality product.
    TQM6 – There are clear quality plans and programmers throughout the company.
    RFT1 – Reviews are carried out to ensure the working procedures of each area are being complied with.
    RFT2 – Ensures the proper functioning of the processes to avoid defects.
    RFT3 – Compliance with quality standards is verified with a zero-defect approach.
    RFT4 – There is a standardized protocol for sampling when you want to do an analysis.
    RFT5 – Training and awareness is carried out in relation to the quality and need to do well the activities.
    RFT6 – The decrease in waste is reported as a benefit of doing the tasks right.
    RFT7 – Customer expectations for quality and delivery times are met.
    W1 – Frequently reduced waits in the supply chain.
    W2 – Inventory levels are low throughout the process.
    W3 – The internal flow of materials is efficient and continuous between operations.
    W4 – Product rework is reduced to the acceptable minimum.
    W5 – The implementation of improvements to reduce waste is encouraged.
    W6 – Seeks to minimize the transport of material.
    W7 – Training and awareness is carried out in relation to the quality and need to do the activities well at the first time.
    W8 – Waste is identified in the production process and supply chain.
    BRC1 – There is a reduction in the cost of acquiring materials.
    BRC2 – There is a reduction in the cost of using energy.
    BRC3 – There is a reduction in the rate for treatment and dumping of waste.
    BRC4 – There has been a reduction of the penalty for environmental mishaps.
    BRC5 – There has been an average increase in sales and investment in the last two years.
    BRC6 – There has been an average health of benefits in the last two years.
    BRC7 – There has been an average change in market share in the last two years.
📝 Explanation:
The data is structured from a survey that assesses various Lean Manufacturing, TQM (Total Quality Management), and waste reduction practices across organizations. Each row represents an individual respondent's rating (probably on a Likert scale from 1 to 5) for a set of statements grouped under specific Lean concepts:

    TQM1–TQM6: Reflect different aspects of Total Quality Management implementation.
    RFT1–RFT7: Cover “Right First Time” practices, focusing on error-free, efficient processes.
    W1–W8: Capture waste elimination techniques and supply chain optimizations.
    BRC1–BRC7: Represent benchmarking-related metrics, reflecting business and environmental benefits such as cost reduction, increased market share, and improved health benefits.
These variables can serve as input features in a machine learning model for predicting business outcomes or classifying lean maturity. For example, BRC5–BRC7 could be treated as potential target variables (e.g., change in market share, sales growth), while the rest can be used as predictors.



Summary: Predictive Modeling for Lean Manufacturing Dataset
✅ Project Objective:
The main goal was to predict key business benefits (BRC5, BRC6, BRC7), such as improvement in investment, health of benefits, and market share, based on Lean Manufacturing indicators like Total Quality Management (TQM), Waste reduction (W), and Right First Time (RFT) practices. This supports strategic decision-making for managers in lean implementation.




Outputs (Target Variables):
These are outcomes or business performance indicators that we want to predict. Based on the labels and meaning, the best candidates for outputs are:
    BRC5 – There has been an average increase in sales and investment in the last two years
    BRC6 – There has been an average health of benefits and benefits in the last two years
    BRC7 – There has been an average change in market share in the last two years

These represent measurable business benefits (sales, health/benefits, market share), and are excellent targets for predictive modeling using machine learning or statistical inference.
✅ Inputs (Features / Independent Variables):

The rest of the variables can be used as input features for modeling:
A. Demographic / Contextual Variables:
    TP – Years of the respondent in the position
    SI – Sector to which it belongs
    GN – Gender
    PE – Position in the Company
B. TQM: Total Quality Management (TQM1 to TQM6)
    These represent how strongly quality practices are implemented in the organization.
C. RFT: Right First Time Practices (RFT1 to RFT7)
    These are practices related to error prevention, standardization, and defect elimination.
D. W: Waste Minimization (W1 to W8)
    These reflect lean waste reduction practices across the value chain.
E. BRC1 to BRC4 – Business Result Contributors
    While BRC5 to BRC7 are the final outcome, BRC1–BRC4 measure cost reductions and penalties. These could be either inputs or intermediate outputs depending on the model design.


Random Forest Classifiers were trained individually for each output variable (BRC5, BRC6, BRC7).
These models used inputs like:
    Demographics (e.g., Gender, Sector, Position)
    Lean Practice indicators (TQM1–TQM6, RFT1–RFT7, W1–W8)
    Baseline benchmarking values (BRC1–BRC4)





Outputs (Target Variables):
These are outcomes or business performance indicators that we want to predict. Based on the labels and meaning, the best candidates for outputs are:
    BRC5 – There has been an average increase in sales and investment in the last two years
    BRC6 – There has been an average health of benefits and benefits in the last two years
    BRC7 – There has been an average change in market share in the last two years
These represent measurable business benefits (sales, health/benefits, market share), and are excellent targets for predictive modeling using machine learning or statistical inference.
✅ Inputs (Features / Independent Variables):
The rest of the variables can be used as input features for modeling:
A. Demographic / Contextual Variables:
    TP – Years of the respondent in the position
    SI – Sector to which it belongs
    GN – Gender
    PE – Position in the Company
B. TQM: Total Quality Management (TQM1 to TQM6)
    These represent how strongly quality practices are implemented in the organization.
C. RFT: Right First Time Practices (RFT1 to RFT7)
    These are practices related to error prevention, standardization, and defect elimination.
D. W: Waste Minimization (W1 to W8)
    These reflect lean waste reduction practices across the value chain.
E. BRC1 to BRC4 – Business Result Contributors
    While BRC5 to BRC7 are the final outcome, BRC1–BRC4 measure cost reductions and penalties. These could be either inputs or intermediate outputs depending on the model design.
