import pandas as pd
import numpy as np


def caselist(df, start, end):
    cl_data = pd.read_csv('caselist.csv', parse_dates=["Admission Date"])

    # format admission dates to computer readable format
    cl_data['Admission Date'] = pd.to_datetime(cl_data['Admission Date'])

    # cast blanks to -1
    cl_data["Age Began Using Drugs"] = cl_data["Age Began Using Drugs"].replace([0], -1)
    cl_data["Age Began Using Alcohol"] = cl_data["Age Began Using Alcohol"].replace([0], -1)

    # if a person has not yet been discharged change discharge elements to NA
    cl_data["Age Began Using Drugs"] = cl_data["Age Began Using Drugs"].replace([0], -1)
    cl_data["Age Began Using Alcohol"] = cl_data["Age Began Using Alcohol"].replace([0], -1)
    cl_data["Discharge Date"] = cl_data["Discharge Date"].replace([np.nan], "NA")
    cl_data = cl_data.fillna(-1)
    cl_data['Discharge Reason'] = cl_data['Discharge Reason'].mask(cl_data['Discharge Reason'].eq(-1),
                                                                   cl_data['Discharge Date'])
    cl_data['Drug Court Case Outcome'] = cl_data['Drug Court Case Outcome'].mask(
        cl_data['Drug Court Case Outcome'].eq(-1), cl_data['Discharge Date'])
    cl_data['Discharge Housing Status'] = cl_data['Discharge Housing Status'].mask(
        cl_data['Discharge Housing Status'].eq(-1), cl_data['Discharge Date'])
    cl_data['Employment Status at Discharge'] = cl_data['Employment Status at Discharge'].mask(
        cl_data['Employment Status at Discharge'].eq(-1), cl_data['Discharge Date'])
    cl_data['Education Level at Discharge'] = cl_data['Education Level at Discharge'].mask(
        cl_data['Education Level at Discharge'].eq(-1), cl_data['Discharge Date'])
    cl_data['Improvement in Education Level'] = cl_data['Improvement in Education Level'].mask(
        cl_data['Improvement in Education Level'].eq(-1), cl_data['Discharge Date'])
    cl_data['Improvement in Employment Status'] = cl_data['Improvement in Employment Status'].mask(
        cl_data['Improvement in Employment Status'].eq(-1), cl_data['Discharge Date'])
    cl_data['Sentence/Disposition at Discharge'] = cl_data['Sentence/Disposition at Discharge'].mask(
        cl_data['Sentence/Disposition at Discharge'].eq(-1), cl_data['Discharge Date'])
    cl_data['Supervision Status at Discharge'] = cl_data['Supervision Status at Discharge'].mask(
        cl_data['Supervision Status at Discharge'].eq(-1), cl_data['Discharge Date'])

    # redact SID, SSN, FDOC
    cl_data.loc[cl_data['SID'] != -1, 'SID'] = "Redacted"
    cl_data.loc[cl_data['FDOC'] != -1, 'FDOC'] = "Redacted"
    cl_data.loc[cl_data['SSN'] != -1, 'SSN'] = "Redacted"

    # delete unneeded rows
    cl_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    cl_data = cl_data[(cl_data['Admission Date'] >= start) & (cl_data['Admission Date'] <= end)]

    # find rows with duplicates, remove duplicates
    cl_report = cl_data[cl_data.values == -1]
    cl_report.drop_duplicates(inplace=True)

    # return results to func
    return cl_report


def caseinfo(df, start, end):
    ci_data = ci_data = pd.read_csv('p_ScreeningExport_GetCaseInformation.csv', parse_dates=["ScreeningDate"])

    # format screening dates to computer readable format
    ci_data['ScreeningDate'] = pd.to_datetime(ci_data['ScreeningDate'])

   # cast blanks to -1
    ci_data = ci_data.fillna(-1)

    # delete unneeded rows
    ci_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    ci_data = ci_data[(ci_data['ScreeningDate'] >= start) & (ci_data['ScreeningDate'] <= end)]

    # find rows with blank and remove duplicate rows
    ci_report = ci_data[ci_data.values == -1]
    ci_report.drop_duplicates(inplace=True)

    #return results to func
    return ci_report

def othercourt(df,start,end):
    oci_data = oci_data = pd.read_csv('p_ScreeningExport_GetOtherCourtInvolvement.csv', parse_dates=["ScreeningDate"])

    # format screening dates to computer readable format
    oci_data['ScreeningDate'] = pd.to_datetime(oci_data['ScreeningDate'])

    # cast blanks to -1
    oci_data = oci_data.fillna(-1)

    # delete unneeded rows
    oci_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    oci_data = oci_data[(oci_data['ScreeningDate'] >= start) & (oci_data['ScreeningDate'] <= end)]

    # find rows with blank and remove duplicate rows
    oci_report = oci_data[oci_data.values == -1]
    oci_report.drop_duplicates(inplace=True)

    #return results to func
    return oci_report

def screeningassessment(df,start,end):
    sa_data = sa_data = pd.read_csv('p_ScreeningExport_GetScreeningAssessments.csv', parse_dates=["ScreeningDate"])

    # format screening dates to computer readable format
    sa_data['ScreeningDate'] = pd.to_datetime(sa_data['ScreeningDate'])

    # cast blanks to -1
    sa_data = sa_data.fillna(-1)

    # delete unneeded rows
    sa_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    sa_data = sa_data[(sa_data['ScreeningDate'] >= start) & (sa_data['ScreeningDate'] <= end)]

    # find rows with blank and remove duplicate rows
    sa_report = sa_data[sa_data.values == -1]
    sa_report.drop_duplicates(inplace=True)

    #return results to func
    return sa_report

def diagnosis(df,start,end):
    dx_data = dx_data = pd.read_csv('p_ScreeningExport_GetDiagnosis.csv', parse_dates=["ScreeningDate"])

    # format screening dates to computer readable format
    dx_data['ScreeningDate'] = pd.to_datetime(dx_data['ScreeningDate'])

    # cast blanks to -1
    dx_data = dx_data.fillna(-1)

    # delete unneeded rows
    dx_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    dx_data = dx_data[(dx_data['ScreeningDate'] >= start) & (dx_data['ScreeningDate'] <= end)]

    # find rows with blank and remove duplicate rows
    dx_report = dx_data[dx_data.values == -1]
    dx_report.drop_duplicates(inplace=True)

    #return results to func
    return dx_report

def relatedparties(df,start,end):
    rp_data = pd.read_csv('p_ScreeningExport_GetRelatedParties.csv', parse_dates=["ScreeningDate"])

    # format screening dates to computer readable format
    rp_data['ScreeningDate'] = pd.to_datetime(rp_data['ScreeningDate'])

    # cast blanks to -1
    rp_data = rp_data.fillna(-1)

    # delete unneeded rows
    rp_data.drop(df, axis=1,inplace=True)

    # choose date range for cohort
    rp_data = rp_data[(rp_data['ScreeningDate'] >= start) & (rp_data['ScreeningDate'] <= end)]

    # find rows with blank and remove duplicate rows
    rp_report = rp_data[rp_data.values == -1]
    rp_report.drop_duplicates(inplace=True)

    #return results to func
    return rp_report

def veteraninfo(df,start,end):
    mi_data = pd.read_csv('p_ScreeningExport_GetVeteranInfo.csv', parse_dates=["ScreeningDate"])

    # format screening dates to computer readable format
    mi_data['ScreeningDate'] = pd.to_datetime(mi_data['ScreeningDate'])

    # cast blanks to -1
    mi_data = mi_data.fillna(-1)

    # delete unneeded rows
    mi_data.drop(df,axis=1, inplace=True)

    # choose date range for cohort
    mi_data = mi_data[(mi_data['ScreeningDate'] >= start) & (mi_data['ScreeningDate'] <= end)]

    # find rows with blank and remove duplicate rows
    mi_report = mi_data[mi_data.values == -1]
    mi_report.drop_duplicates(inplace=True)

    #return results to func
    return mi_report

def militaryreport(df,start,end):
    mil_data = pd.read_csv('MilitaryServiceReport.csv', parse_dates=["AdmissionDate"])

    # format admission dates to computer readable format
    mil_data['AdmissionDate'] = pd.to_datetime(mil_data['AdmissionDate'])

    # cast blanks to -1
    mil_data = mil_data.fillna(-1)

    # if a person is still active military, discharge date is NA
    mil_data["MilitaryDischargeDate"] = mil_data["MilitaryDischargeDate"].replace([np.nan], "NA")

    #####cross reference discharge date and reason######
    mil_data['MilitaryDischargeReason'] = mil_data['MilitaryDischargeReason'].mask(
    mil_data['MilitaryDischargeReason'].eq(-1), mil_data['MilitaryDischargeDate'])
    mil_data.loc[mil_data['MilitaryDischargeReason'] != "NA", 'MilitaryDischargeDate'] = -1

    # delete unneeded rows
    mil_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    mil_data = mil_data[(mil_data['AdmissionDate'] >= start) & (mil_data['AdmissionDate'] <= end)]

    # find rows with blank and remove duplicate rows
    mil_report = mil_data[mil_data.values == -1]
    mil_report.drop_duplicates(inplace=True)

    #return results to func
    return mil_report

def mentalhealth(df,start,end):
    men_data = pd.read_csv('p_ScreeningExport_GetMentalHealthHistory.csv', parse_dates=["ScreeningDate"])

    # format screening dates to computer readable format
    men_data['ScreeningDate'] = pd.to_datetime(men_data['ScreeningDate'])

    # cast blanks to -1
    men_data = men_data.fillna(-1)

    # if the client is competent competency eval elements are NA
    men_data.loc[men_data['DefendantCompetent'] == "Y", 'CompetencyEvaluationOrderedDate'] = "NA"
    men_data.loc[men_data['DefendantCompetent'] == "Y", 'CompetencyEvaluationReceivedDate'] = "NA"
    men_data.loc[men_data['DefendantCompetent'] == "Y", 'AgeOfOnsetOfMentalHealthDisorderYears'] = "NA"

    # delete uneeded rows
    men_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    men_data = men_data[(men_data['ScreeningDate'] >= start) & (men_data['ScreeningDate'] <= end)]

    # find rows with blank and remove duplicate rows
    men_report = men_data[men_data.values == -1]
    men_report.drop_duplicates(inplace=True)

    #return results to func
    return men_report

def familyinfo(df,start,end):
    fam_data = pd.read_csv('p_ScreeningExport_GetFamilyInfo.csv', parse_dates=["ScreeningDate"])

    # format screening dates to computer readable format
    fam_data['ScreeningDate'] = pd.to_datetime(fam_data['ScreeningDate'])

    # cast blanks to -1
    fam_data = fam_data.fillna(-1)

    # delete unneeded rows
    fam_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    fam_data = fam_data[(fam_data['ScreeningDate'] >= start) & (fam_data['ScreeningDate'] <= end)]

    # find rows with blank and remove duplicate rows
    fam_report = fam_data[fam_data.values == -1]
    fam_report.drop_duplicates(inplace=True)

    #return results to func
    return fam_report

def pregnancy(df,start,end):
    p_data = pd.read_csv('PregnancyReport.csv', parse_dates=["AdmissionDate"])

    # format admission dates to computer readable format
    p_data['AdmissionDate'] = pd.to_datetime(p_data['AdmissionDate'])

    # fill in blank rows with -1
    p_data = p_data.fillna(-1)

    # if person is not pregnant outcome and duedate is NA
    p_data.loc[p_data.Pregnant == "No", 'Outcome'] = "NA"
    p_data.loc[p_data.Pregnant == "No", 'DueDate'] = "NA"

    # delete unneeded rows
    p_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    p_data = p_data[(p_data['AdmissionDate'] >= start) & (p_data['AdmissionDate'] <= end)]

    # find rows with blank and remove duplicate rows
    p_report = p_data[p_data.values == -1]
    p_report.drop_duplicates(inplace=True)

    #return results to func
    return p_report

def treatment(df,start,end):
    tx_data = pd.read_csv('TreatmentAttendanceReport.csv', parse_dates=["Admit Date"])

    # format admission dates to computer readable format
    tx_data['Admit Date'] = pd.to_datetime(tx_data['Admit Date'])

   # cast blanks to -1
    tx_data = tx_data.fillna(-1)

    # if the treatment is still active, discharge date and discharge reason is NA
    tx_data.loc[tx_data["Discharge Date"] == -1, 'Discharge Date'] = "NA"
    tx_data.loc[tx_data["Discharge Date"] == "NA", 'Discharge Reason'] = "NA"

    # delete unneeded rows
    tx_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    tx_data = tx_data[(tx_data['Admit Date'] >= start) & (tx_data['Admit Date'] <= end)]

    # find rows with blank and remove duplicate rows
    tx_report = tx_data[tx_data.values == -1]
    tx_report.drop_duplicates(inplace=True)

    #return results to func
    return tx_report

def ancillary(df,start,end):
    a_data = pd.read_csv('AncillaryProgressReport.csv', parse_dates=["AdmissionDate"])

    # format admission dates to computer readable format
    a_data['AdmissionDate'] = pd.to_datetime(a_data['AdmissionDate'])

    # if the service is still ongoing, datended and date ended is NA
    a_data.loc[a_data["Status"] == "Ongoing", 'DateEnded'] = "NA"
    a_data.loc[a_data["Status"] == "In Progress", 'DateEnded'] = "NA"

    # cast blanks to -1
    a_data = a_data.fillna(-1)

    # delete unneeded rows
    a_data.drop(df, axis=1, inplace=True)

    # choose date range for cohort
    a_data = a_data[(a_data['AdmissionDate'] >= start) & (a_data['AdmissionDate'] <= end)]

    # find rows with blank and remove duplicate rows
    a_report = a_data[a_data.values == -1]
    a_report.drop_duplicates(inplace=True)

    #return results to func
    return a_report

def drugtest(df,start=None,end=None):
    dr_data = pd.read_csv('DrugTestingReport.csv')

    # delete unneeded rows
    dr_data.drop(df, axis=1, inplace=True)

    dr_report = dr_data

    #return results to func
    return dr_report

def incentives(df,start=None,end=None):
    in_data = pd.read_csv('IncentiveReport.csv')

    # delete unneeded rows
    in_data.drop(df, axis=1, inplace=True)

    in_report = in_data

    #return results to func
    return in_report

def jail(df,start=None,end=None):
    j_data = pd.read_csv('JailReport.csv', parse_dates=["AdmissionDate"])

    # format admission dates to computer readable format
    j_data['AdmissionDate'] = pd.to_datetime(j_data['AdmissionDate'])

    # if the person has not been discharged yet, jail release is NA
    j_data.loc[j_data["CasePhase"] != "Discharged", 'JailReleasedDate'] = "NA"

    # cast blanks to -1
    j_data = j_data.fillna(-1)

    # delete unneeded rows
    j_data.drop(df, axis=1, inplace=True)

    # find rows with blank and remove duplicate rows
    j_report = j_data[j_data.values == -1]
    j_report.drop_duplicates(inplace=True)

    #return results to func
    return j_report

def suspension(df,start=None,end=None):
    sus_data = pd.read_csv('SuspendedReport.csv')

    # delete unneeded rows 
    sus_data.drop(df, axis=1, inplace=True)

    sus_report = sus_data

    #return results to func
    return sus_report







