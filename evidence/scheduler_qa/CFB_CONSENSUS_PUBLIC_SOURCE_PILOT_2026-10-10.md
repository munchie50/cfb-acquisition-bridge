# CFB consensus public-source pilot — 2026-10-10

Run: CFB_CONSENSUS_SOURCE_PILOT_20261010T153903Z
Scope: three existing conditional-opportunity identities only, not full-slate evaluation or new recommendations.
Collection window bracket: 2026-10-10T15:39:03Z through2026-10-10T15:41:35Z (10:39:03–10:41:35CT). Exact per-call retrieval UTC and bookmaker update times were not returned; do not invent them. All requests maxAge0; successful fetch alone is not current offer/executability proof.
Authority: consensus control29863d6248fb48c1c525f24febb6404efed00597; current indexcf7f5820b176148926ec008409969263cbace4a6.

## Executed source findings
1. VegasInsider generic /college-football/odds/ returned404, scrape01a12678-1ef7-702d-af42-36f5084a4702. Discovered actual /college-football/odds/las-vegas/ returned200, scrape01a12678-89aa-7299-8aac-7f0775041c01. A working URL is not qualification.
2. VegasInsider markdown contains away rows with bookmaker headers but omits corresponding home rows. Matchup markdown also returns repeated team rows spanning full-game and quarter markets. Global fixed-column/first-match parsing is therefore not safe. Never negate an away line and copy its price to invent the home quote.
3. HTML inspection of the AppState matchup, scrape01a12679-5e81-75ee-9516-9093b039102c, showed module-body blur plus member/guest registration gates. This is an observed access/qualification stop. No protected HTML values were parsed into records, saved as observations, used to build consensus or promoted to canonical state. Further access to that source stopped; no sign-in, alternate endpoint, CSS removal or hidden-data extraction. Raw odds bodies from this source are not retained here.
4. Main VegasInsider page has different page-level date labels (October7 last-updated and October10 updated-on); neither establishes per-book update times. Do not mark every constituent current from a page/editorial date. Its named Consensus is a provider-defined most-common line, not our declared non-Caesars median; those methods cannot be silently equated. Provider consensus constituents/exclusion status remain unqualified.
5. DraftKings public NCAAF board returned200, scrape01a12678-2417-700e-89e9-da8074d1a807. Its direct public MiamiOH@UMass and Boise@Fresno game-line regions are readable. AppState identity was not found in this retrieved league board; discovered numeric-event/outcome URL returned404 (scrape01a12678-e557-764a-a96c-f9aa91a641c7). Absence in this extract is not proof the book has no market.
6. FanDuel public AppState event returned200, scrape01a12678-2ffe-757b-a2b7-d2b9c6fd54b2, with identified Game Lines before Alternate/quarter headings. FanDuel UMass public team next-game page returned200, scrape01a12679-8cce-770f-aa46-8ac775894477, with exact opponent/date and side/price. Full-season outcomes and popular props were not ingested. FanDuel Fresno event returned200 but only generic verifying-location content, scrape01a12679-977f-751f-9937-fa162e076aae: content readiness FAIL despite HTTP200. No location/authentication bypass attempted.

## Public research observations only
These values are factual public displays from the bounded window, not canonical accepted current consensus or executable sportsbook offers. Bookmaker-update time UNKNOWN; actual execution NOT_VERIFIED; exact cross-source game-ID lineage still requires separate canonical mapping.

| Matchup / selection | Public direct-book display | Qualified consensus | Caesars execution |
|---|---|---|---|
| Old Dominion @ Appalachian State / AppState | FanDuel -9.5 (-115) | UNAVAILABLE: only one direct-book source here | UNVERIFIED |
| Miami (OH) @ Massachusetts / UMass | DraftKings +6 (-110); FanDuel +5.5 (-104) | UNAVAILABLE: only two direct-book sources here | UNVERIFIED |
| Boise State @ Fresno State / Fresno | DraftKings +7.5 (-108) | UNAVAILABLE: only one direct-book source here; FanDuel not ready | UNVERIFIED |

Sources:
- https://sportsbook.draftkings.com/leagues/football/ncaaf
- https://sportsbook.fanduel.com/football/ncaa-football-games/old-dominion-@-appalachian-state-36137845
- https://sportsbook.fanduel.com/teams/college-football/umass-minutemen/odds
- https://sportsbook.fanduel.com/football/ncaa-football-games/boise-state-@-fresno-state-36137967
- Access/format diagnostic only: https://www.vegasinsider.com/college-football/odds/las-vegas/ and https://www.vegasinsider.com/college-football/matchups/appalachian-state-vs-old-dominion/

## Classification / next safe action
REAL_SOURCE_QUALIFICATION_EXECUTED / CONSENSUS_NOT_ESTABLISHED / CAESARS_NOT_VERIFIED.
No median or Caesars difference computed, no canonical market/decision append and no changed HotSheet recommendation. Existing source acquisition paths can supply public research, but the pilot does not demonstrate three qualified non-Caesars books, source update freshness or actual casino availability.
Next: qualify a third openly accessible operator and exact game/market/selection/time provenance; alternatively explicit authorized access is required before using a gated source. No request to purchase a service, create credentials or change location is made or implied.
Current saved AppState practical cutoff11:00CT, UMass12:00CT and Fresno20:30CT remain unchanged. This research cannot preserve/renew an actionable state after its cutoff. No schedule/run-now mutation, frozen model change, outcome ingestion or historical backfill.
Terminal result RUN_INCOMPLETE for actual qualified consensus/Caesars acquisition, despite successful diagnostic persistence.
