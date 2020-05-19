from ..models import Tarefa


def listar_tarefas(usuario):
    return Tarefa.objects.filter(usuario=usuario).all()


def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(titulo=tarefa.titulo, descricao=tarefa.descricao,
                          data_expiracao=tarefa.data_expiracao, prioridade=tarefa.prioridade,
                          usuario=tarefa.usuario)


def listar_tarefa_id(id):
    return Tarefa.objects.get(id=id)


def editar_tarefa(tarefa_bd, nova_tarefa):
    tarefa_bd.titulo = nova_tarefa.titulo
    tarefa_bd.descricao = nova_tarefa.descricao
    tarefa_bd.data_expiracao = nova_tarefa.data_expiracao
    tarefa_bd.prioridade = nova_tarefa.prioridade
    tarefa_bd.save(force_update=True)


def excluir_tarefa(tarefa_bd):
    tarefa_bd.delete()
