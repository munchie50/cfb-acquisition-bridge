# Week 6 Oct 8 — Saturday market coverage audit (Test Routine v6)

Status: RESEARCH ONLY; not a RUN_PASS or actionable Hot Sheet.

Source: ESPN NCAAF odds https://www.espn.com/college-football/odds retrieved live via Firecrawl maxAge=0 on October 8 evening CT. DraftKings-labelled board; no verified Caesars execution quotes or independently timestamped sportsbook quotes.

Frozen Champion v1.193 / FIRST_FROZEN v1.208 remain immutable. Saturday modeled rows in accepted Oct 7 candidate: 38. ESPN page future Saturday UTC game entries parsed: 46. ESPN includes non-modeled games including Indiana @ Nebraska; never invent a frozen prediction.

## Existing frozen Saturday rows (unchanged)
| Sat 11:00 AM | Arizona @ West Virginia | West Virginia -3.4 | 53.8 | .564 home | -3 (-115) | +3.5 (-122) | INCONCLUSIVE; prospective decision review required |
| Sat 11:00 AM | Texas A&M @ Missouri | Missouri -7.7 | 48.5 | .643 home | +3.5 (-114) | -3.5 (-104) | INCONCLUSIVE; prospective decision review required |
| Sat 11:00 AM | UCF @ Oklahoma State | Oklahoma State -4.3 | 55.1 | .600 home | +10.5 (-108) | -10.5 (-105) | INCONCLUSIVE; prospective decision review required |
| Sat 11:00 AM | North Carolina @ Pittsburgh | Pittsburgh -8.3 | 46.7 | .680 home | +4 (-110) | -3 (-118) | INCONCLUSIVE; prospective decision review required |
| Sat 11:00 AM | Wake Forest @ NC State | NC State -9.3 | 59.3 | .704 home | -3.5 (-102) | +3.5 (-115) | INCONCLUSIVE; prospective decision review required |
| Sat 11:00 AM | Sacramento State @ Bowling Green | Sacramento State -12.7 | 45.8 | .200 home | +7.5 (-108) | -7.5 (-110) | INCONCLUSIVE; prospective decision review required |
| Sat 11:45 AM | South Carolina @ Florida | Florida -7.1 | 61.9 | .693 home | +12.5 (-110) | -11.5 (-108) | INCONCLUSIVE; prospective decision review required |
| Sat 12:00 PM | Old Dominion @ App State | App State -14.3 | 50.1 | .823 home | +10 (-111) | -9.5 (-115) | INCONCLUSIVE; prospective decision review required |
| Sat 1:00 PM | Miami (OH) @ Massachusetts | Massachusetts -14.8 | 54.6 | .818 home | -2 (-115) | +2.5 (-112) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Texas @ Oklahoma | Oklahoma -3.4 | 42.8 | .519 home | -7.5 (-108) | +7.5 (-110) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | UCLA @ Oregon | Oregon -5.1 | 62.8 | .655 home | +11.5 (-110) | -11 (-111) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Stanford @ Notre Dame | Notre Dame -27.6 | 49.3 | .943 home | +38.5 (-111) | -37.5 (-118) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Ole Miss @ Vanderbilt | Vanderbilt -1.9 | 54.7 | .520 home | -9.5 (-111) | +10.5 (-122) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Illinois @ Michigan State | Illinois -4.4 | 50.9 | .359 home | -2.5 (-112) | +2.5 (-105) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Houston @ Kansas State | Kansas State -10.6 | 55.0 | .757 home | +2.5 (-105) | -2.5 (-110) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Eastern Michigan @ Akron | Akron -11.1 | 50.1 | .746 home | -6.5 (-122) | +7 (-115) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Duke @ Georgia Tech | Georgia Tech -0.9 | 47.9 | .568 home | -6.5 (-115) | +7 (-115) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Central Michigan @ Ohio | Central Michigan -1.1 | 48.4 | .483 home | +3 (-111) | -2.5 (-122) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Charlotte @ North Texas | North Texas -7.8 | 62.1 | .669 home | +28.5 (-108) | -28.5 (-106) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Buffalo @ Toledo | Toledo -22.1 | 56.1 | .900 home | +21 (-112) | -20.5 (-114) | INCONCLUSIVE; prospective decision review required |
| Sat 2:30 PM | Kent State @ Western Michigan | Western Michigan -26.7 | 48.3 | .939 home | +14 (-112) | -13.5 (-114) | INCONCLUSIVE; prospective decision review required |
| Sat 3:00 PM | Rice @ East Carolina | East Carolina -0.4 | 44.9 | .544 home | +10 (-110) | -9.5 (-115) | INCONCLUSIVE; prospective decision review required |
| Sat 3:15 PM | Maryland @ Ohio State | Ohio State -11.4 | 56.4 | .759 home | +34.5 (-108) | -34 (-111) | INCONCLUSIVE; prospective decision review required |
| Sat 3:15 PM | Tennessee @ Arkansas | Tennessee -19.0 | 54.7 | .144 home | -13.5 (-110) | +13.5 (-108) | INCONCLUSIVE; prospective decision review required |
| Sat 5:00 PM | San Diego State @ Oregon State | Oregon State -7.7 | 56.9 | .678 home | +15.5 (-111) | -14.5 (-115) | INCONCLUSIVE; prospective decision review required |
| Sat 6:00 PM | Nevada @ UTEP | Nevada -5.1 | 49.6 | .368 home | -8.5 (-114) | +10 (-111) | INCONCLUSIVE; prospective decision review required |
| Sat 6:00 PM | North Dakota State @ UNLV | North Dakota State -8.7 | 46.1 | .273 home | -3 (-118) | +3.5 (-120) | INCONCLUSIVE; prospective decision review required |
| Sat 6:00 PM | LSU @ Kentucky | LSU -2.5 | 55.1 | .453 home | -8.5 (-105) | +8.5 (-108) | INCONCLUSIVE; prospective decision review required |
| Sat 6:30 PM | Air Force @ Northern Illinois | Air Force -16.1 | 48.4 | .180 home | -7.5 (-102) | +7.5 (-112) | INCONCLUSIVE; prospective decision review required |
| Sat 6:30 PM | Syracuse @ Virginia | Virginia -10.1 | 50.8 | .732 home | +9.5 (-110) | -9 (-111) | INCONCLUSIVE; prospective decision review required |
| Sat 6:30 PM | James Madison @ Georgia Southern | James Madison -8.0 | 46.7 | .291 home | -7.5 (-105) | +7.5 (-114) | INCONCLUSIVE; prospective decision review required |
| Sat 6:30 PM | Georgia @ Alabama | Georgia -7.0 | 61.7 | .329 home | +1.5 (-108) | -1.5 (-111) | INCONCLUSIVE; prospective decision review required |
| Sat 6:30 PM | Louisiana @ Louisiana Tech | Louisiana Tech -0.1 | 54.5 | .497 home | +3 (-111) | -2.5 (-122) | INCONCLUSIVE; prospective decision review required |
| Sat 6:30 PM | USC @ Penn State | Penn State -11.8 | 55.0 | .749 home | +1.5 (-108) | -1.5 (-106) | INCONCLUSIVE; prospective decision review required |
| Sat 7:00 PM | Minnesota @ Purdue | Minnesota -5.8 | 58.6 | .345 home | -2.5 (-110) | +2.5 (-105) | INCONCLUSIVE; prospective decision review required |
| Sat 9:15 PM | Kansas @ Utah | Utah -18.9 | 52.2 | .873 home | +15.5 (-110) | -15.5 (-108) | INCONCLUSIVE; prospective decision review required |
| Sat 9:30 PM | Hawai'i @ Arizona State | Arizona State -14.1 | 53.4 | .781 home | +20.5 (-105) | -20.5 (-114) | INCONCLUSIVE; prospective decision review required |
| Sat 9:30 PM | Boise State @ Fresno State | Fresno State -1.6 | 49.6 | .560 home | -6.5 (-108) | +6.5 (-110) | INCONCLUSIVE; prospective decision review required |

## ESPN Saturday source-game index (not automatically reconciled by fuzzy names)
| ESPN slug | Teams from source | Source linked spreads (away/home when extracted) |
|---|---|---|
| texas-am-missouri | Texas A&M AggiesTA&MTA&M @ Missouri TigersMIZMIZ | +3.5 (-115) / -3.5 (-105) |
| arizona-west-virginia | Arizona WildcatsARIZARIZ @ West Virginia MountaineersWVUWVU | -3 (-115) / +3 (-105) |
| ucf-oklahoma-st | UCF KnightsUCFUCF @ Oklahoma State CowboysOKSTOKST | +10.5 (-108) / -10.5 (-112) |
| north-carolina-pitt | North Carolina Tar HeelsUNCUNC @ Pittsburgh PanthersPITTPITT | +3.5 (-108) / -3.5 (-112) |
| wake-forest-nc-state | Wake Forest Demon DeaconsWAKEWAKE @ NC State WolfpackNCSUNCSU | -3.5 (-105) / +3.5 (-115) |
| indiana-nebraska | Indiana HoosiersIUIU @ Nebraska CornhuskersNEBNEB | -7.5 (-105) / +7.5 (-115) |
| tulane-army | Tulane Green WaveTULNTULN @ Army Black KnightsARMYARMY | +3 (-105) / -3 (-115) |
| sacramento-st-bowling-green | Sacramento State HornetsSACSAC @ Bowling Green FalconsBGSUBGSU | +7.5 (-110) / -7.5 (-110) |
| ball-state-northwestern | Ball State CardinalsBALLBALL @ Northwestern WildcatsNUNU | +35.5 (-108) / -35.5 (-112) |
| south-carolina-florida | South Carolina GamecocksSCSC @ Florida GatorsFLAFLA | +11.5 (-112) / -11.5 (-108) |
| old-dominion-app-state | Old Dominion MonarchsODUODU @ App State MountaineersAPPAPP | +9.5 (-105) / -9.5 (-115) |
| miami-oh-umass | Miami (OH) RedHawksM-OHM-OH @ Massachusetts MinutemenMASSMASS | -2.5 (-108) / +2.5 (-112) |
| texas-oklahoma | Texas LonghornsTEXTEX @ Oklahoma SoonersOUOU | -7.5 (-110) / +7.5 (-110) |
| ole-miss-vanderbilt | Ole Miss RebelsMISSMISS @ Vanderbilt CommodoresVANVAN | -9.5 (-108) / +9.5 (-112) |
| houston-kansas-st | Houston CougarsHOUHOU @ Kansas State WildcatsKSUKSU | +2.5 (-105) / -2.5 (-115) |
| duke-georgia-tech | Duke Blue DevilsDUKEDUKE @ Georgia Tech Yellow JacketsGTGT | -6.5 (-115) / +6.5 (-105) |
| stanford-notre-dame | Stanford CardinalSTANSTAN @ Notre Dame Fighting IrishNDND | +39.5 (-115) / -39.5 (-105) |
| virginia-tech-california | Virginia Tech HokiesVTVT @ California Golden BearsCALCAL | -10 (-110) / +10 (-110) |
| illinois-michigan-st | Illinois Fighting IlliniILLILL @ Michigan State SpartansMSUMSU | -2.5 (-120) / +2.5 (+100) |
| ucla-oregon | UCLA BruinsUCLAUCLA @ Oregon DucksOREORE | +11.5 (-110) / -11.5 (-110) |
| charlotte-north-texas | Charlotte 49ersCLTCLT @ North Texas Mean GreenUNTUNT | +28.5 (-108) / -28.5 (-112) |
| tulsa-navy | Tulsa Golden HurricaneTLSATLSA @ Navy MidshipmenNAVYNAVY | +1.5 (-105) / -1.5 (-115) |
| e-michigan-akron | Eastern Michigan EaglesEMUEMU @ Akron ZipsAKRAKR | -6.5 (-118) / +6.5 (-102) |
| buffalo-toledo | Buffalo BullsBUFFBUFF @ Toledo RocketsTOLTOL | +21 (-112) / -21 (-108) |
| c-michigan-ohio | Central Michigan ChippewasCMUCMU @ Ohio BobcatsOHIOOHIO | +3 (-112) / -3 (-108) |
| kent-state-w-michigan | Kent State Golden FlashesKENTKENT @ Western Michigan BroncosWMUWMU | +13.5 (+100) / -13.5 (-120) |
| uconn-temple | UConn HuskiesCONNCONN @ Temple OwlsTEMTEM | +3.5 (-108) / -3.5 (-112) |
| rice-east-carolina | Rice OwlsRICERICE @ East Carolina PiratesECUECU | +10 (-112) / -10 (-108) |
| tennessee-arkansas | Tennessee VolunteersTENNTENN @ Arkansas RazorbacksARKARK | -13.5 (-110) / +13.5 (-110) |
| maryland-ohio-state | Maryland TerrapinsMDMD @ Ohio State BuckeyesOSUOSU | +32.5 (-110) / -32.5 (-110) |
| san-diego-st-oregon-st | San Diego State AztecsSDSUSDSU @ Oregon State BeaversORSTORST | +15.5 (-108) / -15.5 (-112) |
| lsu-kentucky | LSU TigersLSULSU @ Kentucky WildcatsUKUK | -8.5 (-112) / +8.5 (-108) |
| uab-memphis | UAB BlazersUABUAB @ Memphis TigersMEMMEM | +14 (-108) / -14 (-112) |
| nevada-utep | Nevada Wolf PackNEVNEV @ UTEP MinersUTEPUTEP | -10 (-108) / +10 (-112) |
| n-dakota-st-unlv | North Dakota State BisonNDSUNDSU @ UNLV RebelsUNLVUNLV | -3 (-118) / +3 (-102) |
| coastal-marshall | Coastal Carolina ChanticleersCCUCCU @ Marshall Thundering HerdMRSHMRSH | +4 (-112) / -4 (-108) |
| georgia-alabama | Georgia BulldogsUGAUGA @ Alabama Crimson TideALAALA | +1.5 (-108) / -1.5 (-112) |
| syracuse-virginia | Syracuse OrangeSYRSYR @ Virginia CavaliersUVAUVA | +10 (-110) / -10 (-110) |
| usc-penn-state | USC TrojansUSCUSC @ Penn State Nittany LionsPSUPSU | +1.5 (-112) / -1.5 (-108) |
| air-force-n-illinois | Air Force FalconsAFAAFA @ Northern Illinois HuskiesNIUNIU | -7.5 (-108) / +7.5 (-112) |
| james-madison-ga-southern | James Madison DukesJMUJMU @ Georgia Southern EaglesGASOGASO | -7.5 (-105) / +7.5 (-115) |
| louisiana-louisiana-tech | Louisiana Ragin' CajunsULUL @ Louisiana Tech BulldogsLTLT | +3 (-112) / -3 (-108) |
| minnesota-purdue | Minnesota Golden GophersMINNMINN @ Purdue BoilermakersPURPUR | -2.5 (-110) / +2.5 (-110) |
| kansas-utah | Kansas JayhawksKUKU @ Utah UtesUTAHUTAH | +15.5 (-110) / -15.5 (-110) |
| hawaii-arizona-st | Hawai'i Rainbow WarriorsHAWHAW @ Arizona State Sun DevilsASUASU | +20.5 (-105) / -20.5 (-115) |
| boise-st-fresno-st | Boise State BroncosBOISBOIS @ Fresno State BulldogsFRESFRES | -6.5 (-110) / +6.5 (-110) |

## Required reconciliation gate
Exact-match each of 38 frozen Saturday game identities and kickoff times to source IDs; investigate unmatched/missing games, never infer coverage from counts alone. Then qualify timestamped market prices, prices/executability, decision maturity, append-only canonical ledger changes, full Hot Sheet and terminal readback+separate closure. No bet or canonical state change earned by this audit.
