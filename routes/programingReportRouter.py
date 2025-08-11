from schemas.programingReportSchema import ProgramingReportSchema, ProgramingReportPublic
from services.programingReportService import ProgramingReportService
from services.authService import AuthService
from fastapi import APIRouter, Depends
from http import HTTPStatus

service = ProgramingReportService()
auth_service = AuthService()
router = APIRouter(
    prefix='/programingReport',
    tags=['ProgramingReport Endpoints'],
    dependencies=[Depends(auth_service.get_current_user)]
)

@router.get('/getAll', status_code=HTTPStatus.OK)
def getAllProgramingReport():
    try: 
        programingReport = service.getAllInputOutputOfWires()
        return programingReport
    except:
        return HTTPStatus.UNPROCESSABLE_ENTITY

@router.get('/{programing_report_id}', status_code=HTTPStatus.OK, response_model=ProgramingReportPublic)
def getProgramingReportById(programing_report_id: int):
    try: 
        programingReport = service.getProgramingReportById(programing_report_id)
        return programingReport
    except:
        return HTTPStatus.NOT_FOUND