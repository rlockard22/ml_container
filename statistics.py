def stats():
    ms = "Model Statistics:                                                                                                  "
    blank ="                                                                                                                 "
    tp = "True Positives: 40                                                                                                 "
    fp = "False Positives: 9                                                                                                 "
    fn = "False Negatives: 3                                                                                                 "
    tn = "True Negatives: 44                                                                                                 "
    a = "Accuracy:    .8750                                                                                                    "
    p = "Precision:   .8163                                                                                                    " 
    r = "Recall:      .9302                                                                                                       "
    f1 = "F1 Score:    .8695"
    my_str = ms + blank + tp + blank + fp + blank + fn + blank + tn + blank + a + blank + p + blank + r + blank + f1
    return(my_str)