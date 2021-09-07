import pandas as pd
import numpy as np
from xlsxwriter.utility import xl_rowcol_to_cell
from basefunctions import *

# ----------------------------------------------FILL IN THE INFORMATION HERE-----------------------------------------------------
# start  is the beginning of the auditing period and end is the end of the monitoring period. Date format is (year,month,day).
start = pd.Timestamp(2020, 1, 1)
end = pd.Timestamp(2021, 7, 30)
# report_name will be the name of the excel file generated be sure to remember to include .xslx at the end
report_name = "ECC-DDC-Test_Court_Audit.xlsx"
# ----------------------------------------------DONT CHANGE ANYTHING BEYOND THIS POINT---------------------------------------------------


# -------------------------------Declare Queries----------------------------------
caselist_str = ["Age at Screening", "Primary Offense", "Drug Court Case Outcome", "Sentence/Disposition at Screening",
                "Primary Offense Charge Code", "Offense Category", "Offense Date", "Court Program Approach",
                "Incident Offense", "Prior Adjudications", "FDOC", "Current Age",
                "Days From Acceptance to SA Treatment", "Days From Arrest to SA Treatment", "Days In Jail",
                "Days In Jail By Bench Warrant",
                "Days In Jail By Drug Court Sanction", "SID", "Days In Jail By New Offense",
                "Days In Jail By Pre-Admission", "Days of 12 Step Program", "Days Rearrested in Program",
                "Drug Court Control Group", "First Treatment Date", "History of IV Use",
                "In SA Treatment Program At Screening", "IV Drug User", "Marital Status at Screening",
                "Medication Compliance", "Medical Insurance Status", "Number of 12 Step Program Meetings Attended",
                "Number of Bench Warrants", "Number of Days in Drug Court",
                "Days Rearrested Post Program", "Blood Alcohol Content", "CaseStatus", "Zip",
                "Recommended Treatment Modality At Screening", "Arrest Date", "Number of Days in Phase I",
                "Number of Days in Phase II", "Number of Days in Phase III", "Number of Days in Phase IV",
                "Number of Days in Phase IV",
                "Number of Felonies", "Number of Incentives", "Number of Monitoring with Contact Made - No Violation",
                "Number of Overall Positive Drug Tests", "Number of Other Offense",
                "Number of Misdemeanors", "Number of Sanctions", "Number of Status Offenses",
                "Number of Scheduled Drug Court Reviews", "Percent of Positive Drug Tests",
                "Positive Drug Test In Program",
                "1st Positive Drug Test (In Program)", "Reoffend Status Offense In Program",
                "Reoffend Status Offense Post Program", "Retention Days", "Deceased Date",
                "Number Of Ancillary Sessions",
                "Number of Sessions", "SA Early Intervention/Education", "Primary Offense Charge Code",
                "SA Intensive Outpatient", "SA Outpatient", "SA Outpatient Detox", "SA Residential",
                "SA Sub Acute Detox",
                "SA Treatment Contact Hours", "Qualifying Sentencing Score", "Rearrest Date in Program",
                "Rearrest Date Post Program", "Rearrest in Program", "Case Management/Support Coordination Days",
                "Co-occurring Treatment Service Days", "MH Treatment Contact Hours",
                "MH - Doctor/Medication Review Hours", "MH - Assertive Community Treatment (ACT) Hours",
                "MH - Case Management/Support Coordination Hours",
                "MH - Inpatient Hospitalization/Partial Day Hospitalization Hours",
                "MH - Co-occurring Treatment Services Hours",
                "MH - Therapy Services Hours", "ClientID", "PersonGUID", "MH - Residential Hours",
                "MH - Crisis Residential/Intensive Crisis Stabilization Hours",
                "MH - Employment Services Hours", "MH - Community Based Services Hours", "Total Number of Drug Tests",
                "Days From Referral To Screening", "Days From Screening To Acceptance", "PlacedInFosterHome",
                "Sobriety Days", "Drug of Choice-Secondary", "Drug of Choice-Tertiary", "Ethnicity",
                "Improvement in Mental Health", "Improvement in Quality of Life", "Prior Substance Abuse",
                "Substance Abuse Disorder at Screening", "Drivers License Status",
                "Convicted Offense Category in Program", "FullName", "CourtID", "ADDRESS", "CaseID",
                "Prior Subsance Abuse Treatment"]

diagnosis_str = ["ScreeningID","LastName","FirstName", "MiddleName","DOB", "SecondaryDiagnosis","OtherDiagnosis1",
                 "OtherDiagnosis2", "OtherDiagnosis3"]


othercourt_str = ["ScreeningID", "LastName", "FirstName", "MiddleName", "DOB", "OutstandingWarrantStatus",
                  "ProbationStatus", "PendingCriminalOffenses", "PriorAdjudications", "PreConvictionNonDomestic",
                  "PreConvictionDomestic", "PreCourtFailToAppear", "PreDrugCourtParticipation",
                  "PreDrugCourtParticipationOther"]

screeningassessment_str = ["ScreeningID", "LastName", "FirstName", "Gender", "Ethnicity", "MiddleName", "DOB",
                           "ScreeningCaseManager", "SecondaryDrugOfChoice", "TertiaryDrugOfChoice", "Comment",
                           "ViolenceRisk", "RecidivismRisk", "FailToAppearRisk", "CommunityNonCompRisk", "OverallRisk",
                           "OverallRiskOther", "ViolenceRiskOther", "RecidivismRiskOther",
                           "FailToAppearRiskOther", "CommunityNonCompRiskOther", "CriminalRecidivismRisk",
                           "FamilyParenting", "EducationEmployement", "PeerRelations", "SubstanceAbuse",
                           "LeisureRecreation",
                           "PersonalityBehavior", "AttitudesOrientation", "AssessmentType", "ToolAdministeredOther",
                           "Score", "PrimaryDiagnosis", "SecondaryDiagnosis", "IVDrugUser", "TimingOfAdministration"]

relatedparties_str = ["DOB", "ScreeningID", "LastName", "FirstName", "MiddleName", "RelatedPartyDOB", "Gender",
                      "Ethnicity", "Address1", "City", "State", "InfantWithPrenatalSubstanceExposure",
                      "LivingSituation", "ChildCurrentCustodyStatus", "CurrentChildSupport", "Issues", "Attorney"]

veteraninfo_str = ["DOB", "ScreeningID", "LastName", "FirstName", "MiddleName", "Participant",
                   "EnlistmentOrCommissioningDate", "MilitaryOccupationalSpecialty",
                   "DateofMilitaryDischarge", "MilitaryDischargeStatus", "DetailsOfDischarge", "MilitaryRank",
                   "HasServedInUSMilitary", "ConvictionsPriorToMilitaryService", "DDForm214OrOtherSource",
                   "ConvictionsPriorToMilitaryServiceHighestOffense",
                   "AwardsAndDecorations", "RankReduction", "MilitaryIncarceration", "DeployedAbroad", "CombatZone",
                   "CombatZoneStationedOutcome", "WitnessorInvolvementNumberOfTimes", "PTSD", "PTSDDetails",
                   "TBI", "TBIDetails", "IED_HME", "IED_HME_Details", "MST", "MSTDetails", "SentToVAVJOReferralDate",
                   "VeteransAssociationOrGroupMembership", "VeteransAssociationOrGroupMembershipDetails",
                   "ReceivingDisabilityCompensationFromtheVAPercentDisabled", "UtilizingServicesFromTheVetCenter",
                   "ReceivingDisabilityCompensationFromtheVA", "UtilizingServicesFromTheVetCenterDetails",
                   "HasSuicideRisk"]

militaryreport_str = ["CaseID", "Clerk Case Number", "ClientID", "FullName", "Gender", "Race", "DOB", "CaseManager",
                      "Judge", "CasePhase", "CaseStatus", "MilitaryRank",
                      "Months Deployed Abroad", "Deployment Location", "Occupational Specialty", "Years of Service",
                      "Suicide Risk", "Enlistment Date", "Conviction prior to Military", "Awards & Decorations",
                      "Discplinary Action/Rank Reduction", "Military Incarceration", "Number of Deployments abroad",
                      "Conflict Eras of Service", "Number of Times Witness or Involvement",
                      "Date Assessment Received from VA/VJO",
                      "Veterans Association Membership", "Disability Compensation from VA", "Vet Center Utilization",
                      "Veteran Mentor Assigned", "Veteran Mentor Name", "Veteran Mentor Assigned Date"
                      ]

mentalhealth_str = ["DOB", "ScreeningID", "LastName", "FirstName", "MiddleName", "ReferralInformationSummary",
                    "LevelOfCare", "RelatedMentalIllness"]

familyinfo_str = ["DOB", "ScreeningID", "LastName", "FirstName", "MiddleName", "NumberOfDependantChildren",
                  "ChildCustodayOfAllChildrenAtAdmission",
                  "ChildVisitationRightsOfAllChildrenAtAdmission"]

pregnancy_str = ["CaseManager", "Clerk Case Number", "FullName", "Judge", "Gender", "ChildDOB",
                 "CurrentMedicalConditions", "PharmacologicalIntervention", "PharmacologicalInterventionComment",
                 "CurrentMedications", "HistoryOfMedicalConditions", "MedicalHealthNotes"
                 ]

treatment_str = [ "Case Manager","Full Name", "Judge", "Race","DOB", "Gender", "Case Status","Service Units",
                  "TreatmentFor", "Session(s)", "Missed Sessions"]

ancillary_str = [ "CaseManager","FullName", "Judge", "Race","DOB", "Gender", "CaseStatus",  "ServiceUnits",
                  "ContactHours", "ServiceFor","Sessions", "MissedSessions"]

drugtest_str = ["Clerk Case Number", "FullName", "Judge", "CaseManager"]

incentive_str = ["Clerk Case Number", "AdmissionDate","FullName","CasePhase","Gender", "Notes", "Details",
                 "DOB", "Judge", "Ethnicity-HispanicLatinoOrSpanishOrigin","CaseManager"]



# ------------------call base functions and get reports-----------------------------------
caselist_report = caselist(caselist_str, start, end)
othercourt_report = othercourt(othercourt_str, start, end)
screeningassessment_report = screeningassessment(screeningassessment_str, start, end)
diagnosis_report = diagnosis(diagnosis_str, start, end)
veteraninfo_report = veteraninfo(veteraninfo_str, start, end)
relatedparties_report = relatedparties(relatedparties_str, start, end)
militaryreport_report = militaryreport(militaryreport_str, start, end)
mentalhealth_report = mentalhealth(mentalhealth_str, start, end)
familyinfo_report = familyinfo(familyinfo_str, start, end)
pregnancy_report = pregnancy(pregnancy_str, start, end)
treatment_report = treatment(treatment_str, start, end)
ancillary_report = ancillary(ancillary_str, start, end)
drugtest_report = drugtest(drugtest_str)
incentive_report = incentives(incentive_str)

# -------------------------------- BUILD FINAL REPORT------------------------------------------------
def formatter(sheet):
    worksheet = writer.sheets[sheet]
    worksheet.conditional_format('A1:EP15000', {
        'type': 'cell',
        'criteria': '==',
        'value': -1,
        'format': redfill})


writer = pd.ExcelWriter(report_name, engine='xlsxwriter')
caselist_report.to_excel(writer, index=False, sheet_name="caselist")
othercourt_report.to_excel(writer, index=False, sheet_name='othercourtinvolvement')
screeningassessment_report.to_excel(writer, index=False, sheet_name='screeningassessment')
mentalhealth_report.to_excel(writer, index=False, sheet_name='mentalhealth')
diagnosis_report.to_excel(writer, index=False, sheet_name='diagnosis')
relatedparties_report.to_excel(writer, index=False, sheet_name='relatedparties')
familyinfo_report.to_excel(writer, index=False, sheet_name='familyinformation')
veteraninfo_report.to_excel(writer, index=False, sheet_name='screening-military')
militaryreport_report.to_excel(writer, index=False, sheet_name='military')
pregnancy_report.to_excel(writer, index=False, sheet_name='pregnancy')
treatment_report.to_excel(writer, index=False, sheet_name='treatmentattendance')
ancillary_report.to_excel(writer, index=False, sheet_name='ancillaryprogress')
drugtest_report.to_excel(writer, index=False, sheet_name='drugtests')
incentive_report.to_excel(writer, index=False, sheet_name='incentives')

workbook = writer.book
redfill = workbook.add_format({'bg_color': '#FFC7CE'})
fill_list = ['caselist',  'othercourtinvolvement', "screeningassessment", 'diagnosis',
             'relatedparties', "screening-military", "military", 'mentalhealth', 'familyinformation', 'pregnancy',
             'treatmentattendance', 'ancillaryprogress', "drugtests", 'incentives', ]
for i in fill_list:
    formatter(i)
writer.save()
