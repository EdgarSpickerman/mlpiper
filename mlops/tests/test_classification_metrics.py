import pytest
import sklearn
from sklearn import metrics

from parallelm.mlops import mlops as pm
from parallelm.mlops.metrics_constants import ClassificationMetrics
from parallelm.mlops.mlops_exception import MLOpsStatisticsException
from parallelm.mlops.mlops_mode import MLOpsMode


def test_mlops_accuracy_score_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    accuracy_score = metrics.accuracy_score(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.ACCURACY_SCORE, accuracy_score)

    # second way
    pm.metrics.accuracy_score(y_true=labels_actual, y_pred=labels_pred)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.ACCURACY_SCORE, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_pred_missing_values = [0, 0, 0, 1]
        pm.metrics.accuracy_score(y_true=labels_actual, y_pred=labels_pred_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.accuracy_score(y_true=labels_actual,
                              y_pred=labels_pred,
                              sample_weight=sample_weight)

    pm.done()


def test_mlops_auc_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    fpr, tpr, thresholds = sklearn.metrics.roc_curve(labels_actual, labels_pred, pos_label=2)
    auc = sklearn.metrics.auc(fpr, tpr)

    # first way
    pm.set_stat(ClassificationMetrics.AUC, auc)

    # second way
    pm.metrics.auc(x=fpr, y=tpr)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.AUC, [1, 2, 3])

    pm.done()


def test_mlops_bas_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    bas = sklearn.metrics.balanced_accuracy_score(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.BALANCED_ACCURACY_SCORE, bas)

    # second way
    pm.metrics.balanced_accuracy_score(y_true=labels_actual, y_pred=labels_pred)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.BALANCED_ACCURACY_SCORE, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_pred_missing_values = [0, 0, 0, 1]
        pm.metrics.balanced_accuracy_score(y_true=labels_actual, y_pred=labels_pred_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.balanced_accuracy_score(y_true=labels_actual,
                                       y_pred=labels_pred,
                                       sample_weight=sample_weight)

    pm.done()


def test_mlops_bsl_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_actual = [1, 0, 1, 1, 1, 0]
    labels_pred_prob = [0.9, 0.8, 0.7, 0.9, 0.75, 1]

    bsl = sklearn.metrics.brier_score_loss(labels_actual, labels_pred_prob)

    # first way
    pm.set_stat(ClassificationMetrics.BRIER_SCORE_LOSS, bsl)

    # second way
    pm.metrics.brier_score_loss(y_true=labels_actual, y_prob=labels_pred_prob)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.BRIER_SCORE_LOSS, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [0, 0, 0, 1]
        pm.metrics.brier_score_loss(y_true=labels_actual, y_prob=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.brier_score_loss(y_true=labels_actual,
                                y_prob=labels_pred_prob,
                                sample_weight=sample_weight)

    pm.done()


def test_mlops_classification_report_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    cr = metrics.classification_report(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.CLASSIFICATION_REPORT, cr)

    # second way
    pm.metrics.classification_report(y_true=labels_actual, y_pred=labels_pred)

    # should throw error if empty string is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.CLASSIFICATION_REPORT, "")

    # should throw error if None string is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.CLASSIFICATION_REPORT, None)

    # should throw error if weird string
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.CLASSIFICATION_REPORT, "Hello ParallelM")

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_pred_missing_values = [0, 0, 0, 1]
        pm.metrics.classification_report(y_true=labels_actual, y_pred=labels_pred_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]
    target_names = ["class Yes", "class No"]
    # testing with sample weights as well
    pm.metrics.classification_report(y_true=labels_actual,
                                     y_pred=labels_pred,
                                     target_names=target_names,
                                     sample_weight=sample_weight)

    pm.done()


def test_mlops_cks_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    cks = sklearn.metrics.cohen_kappa_score(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.COHEN_KAPPA_SCORE, cks)

    # second way
    pm.metrics.cohen_kappa_score(y1=labels_actual, y2=labels_pred)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.COHEN_KAPPA_SCORE, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [0, 0, 0, 1]
        pm.metrics.cohen_kappa_score(y1=labels_actual, y2=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.cohen_kappa_score(y1=labels_actual,
                                 y2=labels_pred,
                                 sample_weight=sample_weight)

    # testing with weights as well
    pm.metrics.cohen_kappa_score(y1=labels_actual,
                                 y2=labels_pred,
                                 sample_weight=sample_weight,
                                 weights="linear")

    pm.done()


def test_mlops_confusion_metrics_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]
    labels_ordered = [0, 1]

    cm = metrics.confusion_matrix(labels_actual, labels_pred, labels=labels_ordered)

    # first way
    pm.set_stat(ClassificationMetrics.CONFUSION_MATRIX, cm, labels=labels_ordered)

    # second way
    pm.metrics.confusion_matrix(y_true=labels_actual, y_pred=labels_pred, labels=labels_ordered)

    # should throw error if labels are not provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.CONFUSION_MATRIX, cm)

    with pytest.raises(MLOpsStatisticsException):
        pm.metrics.confusion_matrix(y_true=labels_actual, y_pred=labels_pred, labels=None)

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_pred_missing_values = [0, 0, 0, 1]
        pm.metrics.confusion_matrix(y_true=labels_actual, y_pred=labels_pred_missing_values, labels=None)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.confusion_matrix(y_true=labels_actual,
                                y_pred=labels_pred,
                                labels=labels_ordered,
                                sample_weight=sample_weight)

    pm.done()


def test_mlops_f1_score_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    f1 = sklearn.metrics.f1_score(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.F1_SCORE, f1)
    pm.set_stat(ClassificationMetrics.F1_SCORE, [1, 2, 3])

    # second way
    pm.metrics.f1_score(y_true=labels_actual, y_pred=labels_pred)

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [0, 0, 0, 1]
        pm.metrics.f1_score(y_true=labels_actual, y_pred=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.f1_score(y_true=labels_actual,
                        y_pred=labels_pred,
                        sample_weight=sample_weight)

    labels_pred_multiclass = [1, 0, 2, 1, 1, 2]
    labels_actual_multiclass = [0, 1, 1, 0, 2, 0]

    f1_score = pm.metrics.f1_score(y_true=labels_actual_multiclass,
                                   y_pred=labels_pred_multiclass,
                                   labels=[0, 1, 2],
                                   average=None)

    assert len(f1_score) == 3

    pm.done()


def test_mlops_fbeta_score_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    fbeta_score = sklearn.metrics.fbeta_score(labels_actual, labels_pred, beta=0.5)

    # first way
    pm.set_stat(ClassificationMetrics.FBETA_SCORE, fbeta_score)
    pm.set_stat(ClassificationMetrics.FBETA_SCORE, [1, 2, 3])

    # second way
    pm.metrics.fbeta_score(y_true=labels_actual, y_pred=labels_pred, beta=0.5)

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [0, 0, 0, 1]
        pm.metrics.fbeta_score(y_true=labels_actual, y_pred=labels_prob_missing_values, beta=0.5)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.fbeta_score(y_true=labels_actual,
                           y_pred=labels_pred,
                           sample_weight=sample_weight,
                           beta=0.5)

    labels_pred_multiclass = [1, 0, 2, 1, 1, 2]
    labels_actual_multiclass = [0, 1, 1, 0, 2, 0]

    fbeta_score = pm.metrics.fbeta_score(y_true=labels_actual_multiclass,
                                         y_pred=labels_pred_multiclass,
                                         labels=[0, 1, 2],
                                         average=None,
                                         beta=0.5)

    assert len(fbeta_score) == 3

    pm.done()


def test_mlops_hamming_loss_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    hamming_loss = sklearn.metrics.hamming_loss(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.HAMMING_LOSS, hamming_loss)

    # second way
    pm.metrics.hamming_loss(labels_actual, labels_pred)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.HAMMING_LOSS, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [0, 0, 0, 1]
        pm.metrics.hamming_loss(y_true=labels_actual, y_pred=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.hamming_loss(y_true=labels_actual,
                            y_pred=labels_pred,
                            sample_weight=sample_weight)

    pm.done()


def test_mlops_hinge_loss_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred_prob = [0.9, 0.4, 0.6, 0.9, 0.1, 0.9]
    labels_actual = [0, 1, 0, 0, 0, 1]

    hinge_loss = sklearn.metrics.hinge_loss(labels_actual, labels_pred_prob)

    # first way
    pm.set_stat(ClassificationMetrics.HINGE_LOSS, hinge_loss)

    # second way
    pm.metrics.hinge_loss(labels_actual, labels_pred_prob)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.HINGE_LOSS, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [0.0, 0.9, 1.0, 0.85]
        pm.metrics.hinge_loss(y_true=labels_actual, pred_decision=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.hinge_loss(y_true=labels_actual,
                          pred_decision=labels_pred_prob,
                          sample_weight=sample_weight)

    pm.done()


def test_mlops_jaccard_sim_score_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    jss = sklearn.metrics.jaccard_similarity_score(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.JACCARD_SIMILARITY_SCORE, jss)

    # second way
    pm.metrics.jaccard_similarity_score(labels_actual, labels_pred)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.JACCARD_SIMILARITY_SCORE, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [1, 0, 1, 1]
        pm.metrics.jaccard_similarity_score(y_true=labels_actual, y_pred=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.jaccard_similarity_score(y_true=labels_actual,
                                        y_pred=labels_pred,
                                        sample_weight=sample_weight)

    pm.done()


def test_mlops_log_loss_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred_prob = [[0.9, 0.1], [0.6, 0.4], [0.6, 0.4], [0.1, 0.9], [0.1, 0.8], [0.1, 0.9]]
    labels_actual = [0, 1, 0, 0, 0, 1]

    log_loss = sklearn.metrics.log_loss(labels_actual, labels_pred_prob)

    # first way
    pm.set_stat(ClassificationMetrics.LOG_LOSS, log_loss)

    # second way
    pm.metrics.log_loss(labels_actual, labels_pred_prob)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.LOG_LOSS, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [[0.9, 0.1], [0.6, 0.4], [0.6, 0.4]]
        pm.metrics.log_loss(y_true=labels_actual, y_pred=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.log_loss(y_true=labels_actual,
                        y_pred=labels_pred_prob,
                        sample_weight=sample_weight)

    pm.done()


def test_mlops_matthews_corrcoef_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    mcc = sklearn.metrics.matthews_corrcoef(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.MATTHEWS_CORRELATION_COEFFICIENT, mcc)

    # second way
    pm.metrics.matthews_corrcoef(labels_actual, labels_pred)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.MATTHEWS_CORRELATION_COEFFICIENT, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [1, 0, 1, 1]
        pm.metrics.matthews_corrcoef(y_true=labels_actual, y_pred=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.matthews_corrcoef(y_true=labels_actual,
                                 y_pred=labels_pred,
                                 sample_weight=sample_weight)

    pm.done()


def test_mlops_precision_recall_curve_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred_prob = [0.9, 0.4, 0.6, 0.9, 0.1, 0.9]
    labels_actual = [0, 1, 0, 0, 0, 1]

    precision, recall, thresholds = sklearn.metrics.precision_recall_curve(y_true=labels_actual,
                                                                           probas_pred=labels_pred_prob)
    # first way
    pm.set_stat(ClassificationMetrics.PRECISION_RECALL_CURVE, [precision, recall])

    pm.set_stat(ClassificationMetrics.PRECISION_RECALL_CURVE, [precision, recall], legend="Precision Recall")

    # second way
    pm.metrics.precision_recall_curve(y_true=labels_actual,
                                      probas_pred=labels_pred_prob)

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [0.0, 0.9, 1.0, 0.85]
        pm.metrics.precision_recall_curve(y_true=labels_actual,
                                          probas_pred=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.precision_recall_curve(y_true=labels_actual,
                                      probas_pred=labels_pred_prob,
                                      sample_weight=sample_weight)

    # testing with pos label as well
    pm.metrics.precision_recall_curve(y_true=labels_actual,
                                      probas_pred=labels_pred_prob,
                                      sample_weight=sample_weight,
                                      pos_label=1)

    # testing with average as well
    pm.metrics.precision_recall_curve(y_true=labels_actual,
                                      probas_pred=labels_pred_prob,
                                      sample_weight=sample_weight,
                                      pos_label=1,
                                      average="micro")
    pm.done()


def test_mlops_precision_score_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    precision_score = sklearn.metrics.precision_score(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.PRECISION_SCORE, precision_score)

    # second way
    pm.metrics.precision_score(y_true=labels_actual, y_pred=labels_pred)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.precision_score(y_true=labels_actual,
                               y_pred=labels_pred,
                               sample_weight=sample_weight)

    labels_pred_multiclass = [1, 0, 2, 1, 1, 2]
    labels_actual_multiclass = [0, 1, 1, 0, 2, 0]

    # first way where precision score is array of values per class.
    precision_score = sklearn.metrics.precision_score(y_true=labels_actual_multiclass,
                                                      y_pred=labels_pred_multiclass,
                                                      pos_label=2,
                                                      labels=[0, 1, 2],
                                                      average=None)
    pm.set_stat(ClassificationMetrics.PRECISION_SCORE, precision_score)

    # second way
    precision_score = pm.metrics.precision_score(y_true=labels_actual_multiclass,
                                                 y_pred=labels_pred_multiclass,
                                                 pos_label=2,
                                                 labels=[0, 1, 2],
                                                 average=None)

    assert len(precision_score) == 3

    pm.done()


def test_mlops_recall_score_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    recall_score = sklearn.metrics.recall_score(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.RECALL_SCORE, recall_score)

    # second way
    pm.metrics.recall_score(y_true=labels_actual, y_pred=labels_pred)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.recall_score(y_true=labels_actual,
                            y_pred=labels_pred,
                            sample_weight=sample_weight)

    labels_pred_multiclass = [1, 0, 2, 1, 1, 2]
    labels_actual_multiclass = [0, 1, 1, 0, 2, 0]

    # first way where recall score is array of values per class.
    recall_score = sklearn.metrics.recall_score(y_true=labels_actual_multiclass,
                                                y_pred=labels_pred_multiclass,
                                                pos_label=2,
                                                labels=[0, 1, 2],
                                                average=None)
    pm.set_stat(ClassificationMetrics.RECALL_SCORE, recall_score)

    # second way
    recall_score = pm.metrics.recall_score(y_true=labels_actual_multiclass,
                                           y_pred=labels_pred_multiclass,
                                           pos_label=2,
                                           labels=[0, 1, 2],
                                           average=None)

    assert len(recall_score) == 3

    pm.done()


def test_mlops_roc_auc_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred_prob = [0.9, 0.4, 0.6, 0.9, 0.1, 0.9]
    labels_actual = [0, 1, 0, 0, 0, 1]

    roc_auc_score = sklearn.metrics.roc_auc_score(labels_actual, labels_pred_prob)

    # first way
    pm.set_stat(ClassificationMetrics.ROC_AUC_SCORE, roc_auc_score)

    # second way
    pm.metrics.roc_auc_score(labels_actual, labels_pred_prob)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.ROC_AUC_SCORE, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [0.0, 0.9, 1.0, 0.85]
        pm.metrics.roc_auc_score(y_true=labels_actual, y_score=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.roc_auc_score(y_true=labels_actual,
                             y_score=labels_pred_prob,
                             sample_weight=sample_weight)

    pm.done()


def test_mlops_roc_curve_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred_prob = [0.9, 0.4, 0.6, 0.9, 0.1, 0.9]
    labels_actual = [0, 1, 0, 0, 0, 1]

    fpr, tpr, thresholds = sklearn.metrics.roc_curve(labels_actual, labels_pred_prob,
                                                     pos_label=1,
                                                     sample_weight=None,
                                                     drop_intermediate=True)

    roc_auc_score = sklearn.metrics.roc_auc_score(labels_actual, labels_pred_prob)

    graph_label_str = "AUC: {}".format(roc_auc_score)

    # first way
    pm.set_stat(ClassificationMetrics.PRECISION_RECALL_CURVE, [tpr, fpr])

    pm.set_stat(ClassificationMetrics.PRECISION_RECALL_CURVE, [tpr, fpr], legend=graph_label_str)

    # second way
    pm.metrics.roc_curve(labels_actual, labels_pred_prob,
                         pos_label=1,
                         sample_weight=None,
                         drop_intermediate=True)

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [0.0, 0.9, 1.0, 0.85]
        pm.metrics.roc_curve(labels_actual, labels_prob_missing_values,
                             pos_label=1,
                             sample_weight=None,
                             drop_intermediate=True)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.roc_curve(labels_actual, labels_pred_prob,
                         pos_label=1,
                         sample_weight=sample_weight,
                         drop_intermediate=True)

    pm.done()


def test_mlops_zero_one_loss_apis():
    pm.init(ctx=None, mlops_mode=MLOpsMode.STAND_ALONE)

    labels_pred = [1, 0, 1, 1, 1, 0]
    labels_actual = [0, 1, 0, 0, 0, 1]

    zero_one_loss = sklearn.metrics.zero_one_loss(labels_actual, labels_pred)

    # first way
    pm.set_stat(ClassificationMetrics.ZERO_ONE_LOSS, zero_one_loss)

    # second way
    pm.metrics.zero_one_loss(labels_actual, labels_pred)

    # should throw error if not numeric number is provided
    with pytest.raises(MLOpsStatisticsException):
        pm.set_stat(ClassificationMetrics.ZERO_ONE_LOSS, [1, 2, 3])

    # should throw error if labels predicted is different length than actuals
    with pytest.raises(ValueError):
        labels_prob_missing_values = [1, 0, 1, 1]
        pm.metrics.zero_one_loss(y_true=labels_actual, y_pred=labels_prob_missing_values)

    sample_weight = [0.9, 0.1, 0.5, 0.9, 1.0, 0]

    # testing with sample weights as well
    pm.metrics.zero_one_loss(y_true=labels_actual,
                             y_pred=labels_pred,
                             sample_weight=sample_weight)

    # testing with normalization false
    pm.metrics.zero_one_loss(y_true=labels_actual,
                             y_pred=labels_pred,
                             normalize=False,
                             sample_weight=sample_weight)

    pm.done()
