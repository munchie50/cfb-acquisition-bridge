# CFB Engine — Controlled Experimental Capital and Parlay Exposure Contract v1.238

Status: **ACTIVE CONTROLLED-BETA CAPITAL / EXPERIMENT CONTROL**
Date: 2026-09-27
Parents: v1.226, v1.227, v1.231, v1.233, v1.235, v1.236, v1.237

## Authorized starting sandbox capital
Adam authorizes an initial **$20 sandbox investment** for controlled real-money experimental CFB betting evidence.

This is a capital-at-risk ceiling for the sandbox experiment, not a target to spend and not permission to force wagers. Uncommitted capital remains available. The $20 is separate from ordinary production-qualified wagering unless a later authority explicitly combines them.

## Purpose
Use small, controlled real-money exposure to accelerate prospective learning where a betting-layer hypothesis is sufficiently defined to make a reproducible pre-event recommendation but has not yet earned production-qualified maturity.

Low maturity may reduce exposure; it should not automatically hide a useful candidate.

## Capital ledger
Maintain append-only accounting:
- starting sandbox capital;
- available/uncommitted capital;
- committed/open exposure;
- settled wins/losses/returns;
- current sandbox balance;
- cumulative amount risked;
- experiment ID and purpose;
- wager type and exact stake;
- duplicated/correlated exposure;
- recommendation maturity;
- execution evidence;
- qualified close/CLV where available;
- outcome and learning disposition.

Never infer execution from a candidate slip. Only established actual wagers consume real sandbox capital.

## Exposure behavior
The initial practical experimental unit is **$1–$2 when appropriate**, consistent with Adam's stated tolerance. This is not a requirement to bet every candidate and is not an automatic staking formula.

Higher dollar exposure requires stronger evidence and a later governed staking/risk framework. Do not infer authorization for larger experimental stakes merely because the sandbox balance permits them.

Aggregate exposure governs. Multiple wagers sharing the same game, leg, model assumption, or materially correlated risk must be recognized as overlapping exposure rather than treated as independent tiny risks.

If the sandbox balance becomes low, losses cluster around the same unresolved mechanism, source/semantic integrity is uncertain, or exposure concentration becomes material, reduce or pause new experimental exposure pending review. Do not chase losses or increase stake to recover prior losses.

## Time-sensitive recommendation control
Every actionable experimental recommendation must be timestamped and prospective. WAIT requires:
- what information is being awaited;
- why it could change the decision;
- current opportunity/price at risk;
- next trigger/review point;
- latest useful decision point when it can be responsibly stated.

As time passes, continued WAIT requires increasing justification. Transition prospectively to ACT/BET, PASS, or continued WAIT with a concrete reason. Track WAIT outcomes as HELPED, HURT, NEUTRAL, or UNRESOLVED.

No arbitrary universal time threshold is invented here; Beta evidence will inform later thresholds.

## Parlay experimental objective
Parlays are an **asymmetric-upside experimental layer**, not a safety-net layer.

Candidate construction should seek a defensible combination of:
- independently qualifying legs;
- strong available edge evidence under current authority;
- meaningful payout improvement for the added failure points;
- price quality;
- diversification of edge sources where useful;
- correlation/dependence awareness;
- ticket fragility;
- duplicated exposure with singles/other parlays.

Four- and five-leg structures may be explored when the additional legs contribute enough potential reward and remain defensible. Do not add legs merely to increase payout, and do not combine very safe low-value favorites merely to create a high nominal hit rate with trivial reward.

Before calibrated betting probabilities exist, do not manufacture parlay EV, joint hit probability, or independence assumptions. Surface candidates as EXPERIMENTAL LEAN or CONTROLLED BETA RECOMMENDATION at the authority actually earned.

For each candidate preserve:
- constituent legs and prices when qualified;
- reason/edge source for each leg;
- combined offered price/potential payout when qualified;
- maturity/uncertainty;
- known correlation/dependence concerns;
- payout contribution and fragility concerns where supportable;
- corresponding singles alternative/counterfactual;
- overlap with other portfolio exposure;
- exact learning question.

## Recommendation continuity
Once a parlay or other experimental layer can produce reproducible prospective outputs, it should continue producing them each applicable cycle unless a documented blocker invalidates the output. Silence requires a reason.

## Learning value
Every real-money experiment must identify what it is intended to teach. Outcomes are not the only evidence. Review prediction quality, expression choice, price, timing, qualified CLV, construction, correlation/fragility, execution, and singles counterfactual separately.

A win does not prove the method. A loss does not disprove it.

## Weekly review
Sunday Weekly Beta Review must report:
- sandbox starting/current/available balance;
- committed and cumulative experimental exposure;
- experiments and learning questions;
- experimental recommendations not executed;
- parlay structures and singles counterfactuals;
- overlap/concentration;
- WAIT HELPED/HURT/NEUTRAL/UNRESOLVED;
- evidence learned per dollar risked where meaningfully assessable;
- continue/modify/reduce/pause/retire dispositions;
- time-hidden layers and next safe exposure step.

## Locks
- No automatic wager placement.
- Adam retains execution control unless a later explicit authority changes it.
- No loss chasing.
- No retroactive recommendation manufacture.
- No invented probability/EV/confidence.
- No automatic Champion mutation or promotion.
- No use of Adam's wager as Champion model input.
- Source/semantic failures remain fail-closed.

## Initial ledger state
- Sandbox starting capital: **$20.00**
- Current available capital: **$20.00**
- Current committed/open exposure: **$0.00**
- Cumulative established experimental amount risked: **$0.00**
- Established experimental wagers under this authority: **0**

This initial state changes only from established execution evidence; recommendations/candidate slips do not consume capital.

Scientific effect: none on the frozen Beta Champion. This contract authorizes and governs controlled experimental capital exposure and prospective learning around the betting layer.

## October11 funding-versus-execution accounting clarification

Canonicalfunding/money surface is evidence/operational/CFB_MONEY_LEDGER.md; actualwagers remain in evidence/operational/CFB_EXECUTION_LEDGER.md. User clarifiedthepreviouspending“Alsoadd20tomoneyledger” instruction asNEW+20USDfunding, separatefromfour$5betstakes. RecordthisoriginalinstructionONCE, unique funding_id/idempotency_key; a clarification isnotanotherfundingevent. Preserve original pendingstatements ashistorical andsupersede onlytheirambiguousmeaning.

Funding remainsUNASSIGNED betweenproduction/sandbox unlessdirectallocationauthority exists. Actualfundingeventdate/time isunspecified; recordingclock doesnot backdatefunds. Contributions,stakes,expected/result-grade returns,confirmedcashpayments,withdrawals andbudgettransfers aredistinct. Do notdoubledebitfour-ticketstakes, infercashedreturns, ormanufactureanopening/combinedbankrollbalance. User-confirmedfunding isbookkeeping, notanautomatedbanktransfer.

Theinitialsandbox20ceiling/available20/assignedexposure0 remainsunchanged; thisunassignedfunding doesnotauthorize40sandboxcapitalorassignpriorwagers. All15actualexecutions/53.45historicalstakes andfour-ticket20stake/14.55arithmeticreturn/-5.45net remainunchanged. Futuremoneyappend mustdedupebothfunding_id andsourceinstructionkey beforewrite/readback. No model,decision,stake/risk rule,wager,result orschedulechange.


## October11 confirmed ADD20 record integrity / recurring QA detection

Thebookedoriginal+20 funding record mustremainunique anddistinctfromfour-ticket20stake, expectedreturns andcashpayouts. Read-only scripts/cfb_money_ledger_guard.py qualifiescurrentlyapprovedCFB_ORIGINAL_ADD20_FUNDING_001/sourcekey only: strictUSDdecimal/type/schema/duplicateJSON/id/source-key checks, qualifieddirectuserclarification,UNASSIGNEDallocation,unspecifiedactualfundingtime/nonfuture recordingclock,nowager/payout/risk-ceiling flags,unknowncombinedcashbalance, exactrelated4ticket IDs andhistorical15-ID/53.45stake/20relatedstake reference. Reconcile displayedfundingtable/total/count andunique CURRENT_MONEY_LEDGER: selector/sourcehash. Historicalexecutionreference isrecoveredfromcanonicalGithistory, notsilentlysubstitutedwithfutureledgerbytes.

ExistingGitHubQA nowreadsthemoneyledger andruns28record/mutation/source/selector tests. Applicableproducer shouldrunthisqualifiedguard beforepublishingcash-record completionwhenruntimeavailable; postwriteCI isdetection, notproofofprewriteuse. Unknownadditionalfunding/allocation/type/schema/sourceboundary requiresitsownacceptedsource/qualification, notblindreuseorrewritingtheoriginal+20record.

PASS_QUALIFIED_ADD20_FUNDING_RECORD_ONLY certifiesONLYthesequalifiedstructuredrecord/table/reference/binding checks. Itdoesnotauthenticateabanktransfer,provepaid-outreturns/availablecombinedbankroll,authorizefunding/risk changes orcertifyeveryfree-prose financialstatement. Newfundingstillrequiresdirectsourceevidenceandidempotence; sourcekey/metadata cannotself-authorizeit. No existingamount/balance/allocation/ceiling, execution/result, recommendation, task/schedule/model state changed byguardinstallation. Naturalproduceruse pending;moneytransaction remainsoneunassigned+20.
