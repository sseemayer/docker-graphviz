import hug
from hug_middleware_cors import CORSMiddleware
from six import BytesIO
import subprocess
from tempfile import NamedTemporaryFile as ntf

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))


@hug.get_post('/viz.svg', output=hug.output_format.image("svg+xml"))
@hug.get_post('/viz.png', output=hug.output_format.image("png"))
@hug.get_post('/viz.dot', output=hug.output_format.text)
@hug.get_post('/viz.xdot', output=hug.output_format.text)
def demo(
    dot: 'A Graphviz dot document',
    request,
    response,
    algorithm: hug.types.one_of(['dot', 'neato', 'twopi', 'circo', 'fdp', 'sfdp', 'patchwork', 'osage'])='dot',
):

    suffix = request.path.split(".")[-1]

    # Enforce unicode strings
    try:
        dot = dot.decode("utf-8")
    except AttributeError:
        pass

    with ntf(suffix=".dot", mode="w") as f_dot, ntf(mode="r+b") as f_out, ntf(mode="r") as f_err:
        f_dot.write(dot)
        f_dot.flush()

        cmd = [
            algorithm,
            '-T',
            suffix,
            f_dot.name,
            '-o',
            f_out.name
        ]

        proc = subprocess.Popen(cmd, stdout=f_err, stderr=subprocess.STDOUT)

        ret = proc.wait()

        if ret != 0:
            response.status = hug.HTTP_500
            f_err.seek(0)
            return {"status_code": ret, "message": f_err.read()}

        f_out.seek(0)
        out_data = f_out.read()

    return BytesIO(out_data)
